import unittest
from os import path
from flaskr.users import get_all
from mockito import when, mock, unstub
import requests
import datetime
import json
from flaskr.models import db, Clock
from flaskr import create_app
from flaskr.clock import extract_time_intervals

class TestClock(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(path.join(path.dirname(__file__), 'test.db'))
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_punch(self):
        """ Assert a redirection after the registration of a new punch """

        response = self.client.post('/clock/punch/1')
        self.assertEqual(302, response.status_code)


    def test_get_punches(self):
        """ Assert that the response has the keys:
            total_punches: list
            total hours : str 
        """

        resp = self.client.post('/clock/get_punches/1')
        response = resp.json
        self.assertIn('punches', response)
        self.assertIn('total_hours', response)
        self.assertTrue(type(response['punches']) is list)
        self.assertTrue(type(response['total_hours']) is str)


    def test_time_intervals(self):
        """ Assert that the calculations are being made correctly """
        punch_list = [{'time': '2020-09-21T19:00:00.0', 'exit_type': False}, {'time': '2020-09-21T19:15:00.0', 'exit_type': True}]
        time_intervals = extract_time_intervals(punch_list)
        
        # the time diff must be 15min
        self.assertEqual(time_intervals[0].seconds/60, 15.0)

        
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
