from flask import (
    Blueprint, render_template, request, jsonify, redirect, url_for
)

import datetime

from .models import db, Clock, clock_punches_schema

bp = Blueprint('clock', __name__, url_prefix='/clock')


def extract_time_intervals(punches_list: 'list of dicts')-> list:
    diff = []
    for n,punch in enumerate(punches_list):
        if punches_list[n]['exit_type'] == False:
            enter_time = datetime.datetime.strptime(punches_list[n]['time'], '%Y-%m-%dT%H:%M:%S.%f')
            try:
                exit_time = datetime.datetime.strptime(punches_list[n+1]['time'], '%Y-%m-%dT%H:%M:%S.%f')
                diff.append(exit_time - enter_time)
            except:
                pass
    return diff



@bp.route('/punch/<user_id>', methods=['POST'])
def punch(user_id):
    """ Create a new punch action """
    last_record = Clock.query.filter_by(user_id=user_id).order_by(Clock.id.desc()).first()
    if last_record:
        exit_last = last_record.exit_type
        exit_type = not exit_last
    else:
        exit_type = False
    new_punch = Clock(
        user_id= user_id,
        exit_type = exit_type,
        time= datetime.datetime.now()
    )
    db.session.add(new_punch)
    db.session.commit()
    if request.get_json():
        return jsonify({"message":"success"})

    return redirect(url_for('users.get_all'))



@bp.route('/get_punches/<user_id>', methods=('GET', 'POST'))
def get_punches(user_id):
    """ Get the punches for a user with a given id """
    punches = Clock.query.filter_by(user_id=user_id)
    diff = []
    enter_time = []
    exit_time = []
    punches_list = clock_punches_schema.dump(punches)
    time_intervals = extract_time_intervals(punches_list) 
        
    total_hours = sum(time_intervals, datetime.timedelta(0,0))
    if request.method == 'POST':
        return jsonify({"punches": punches_list, "total_hours": str(total_hours)})
    
    return render_template('clock/punches.html', user_id=user_id, punches=punches, total_hours=total_hours)