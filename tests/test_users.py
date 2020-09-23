import unittest
from os import path
from flaskr.users import get_all
from mockito import when, mock, unstub, patch
import requests
import datetime
import json
from flaskr.models import db, User, user_schema
from flaskr import create_app

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(path.join(path.dirname(__file__), 'test.db'))
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_register_user(self):
        """ Register a new user and assert status 200 """

        payload = json.dumps({
            "full_name": "test_user",
            "email": "email@teste.com",
            "cpf": "XXX-XXX"
        })

        response = self.client.post('/users/register', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)

    def test_get_all(self):
        """ Assert that the get all users endpoint returns a list """

        response = self.client.post('users/all')
        self.assertTrue(type(response.json) is list)


    def test_mockito(self):
        """ Test mockito support """
        response = mock({'status_code': 200, 'text': 'Ok'})
        when(self.client).post('user/1').thenReturn(response)
        resp = self.client.post('user/1')
        self.assertEqual(resp.text, 'Ok')

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
