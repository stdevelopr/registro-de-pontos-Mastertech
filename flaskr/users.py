from flask import (
    Blueprint, render_template, request, jsonify, redirect, url_for
)
from datetime import datetime as dt
from .models import db, User, user_schema, users_schema

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/<id>', methods=('GET', 'POST'))
def user_info(id):
    """ Return the info of a user with a given id """
    user = User.query.filter_by(id=id).first()
    if request.method == 'POST':
        return jsonify(user_schema.dump(user))
    return render_template('users/info.html', user=user)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """ Register a new user """
    if request.method == 'POST':
        data = request.get_json() or request.form
        full_name = data['full_name']
        email = data['email']
        cpf = data['cpf']

        new_user = User(
            full_name=full_name,
            cpf=cpf,
            email=email,
            created= dt.now()
        )
        db.session.add(new_user)
        db.session.commit()

        if request.get_json():
            return jsonify({"message": "success"})

        return redirect(url_for('users.get_all'))


    return render_template('users/cadastro.html')

@bp.route('/all', methods=('GET', 'POST'))
def get_all()-> list:
    """ Return a list with all registered users """
    users = User.query.all()
    if request.method == 'POST':
        return jsonify(users_schema.dump(users))
    return render_template('users/list.html', users=users)


@bp.route('/edit/<id>',  methods=('GET', 'POST'))
def edit_user(id):
    """ Edit the info of a user with a given id """
    user = User.query.filter_by(id=id).first()
    if request.method == 'POST':
        data = request.get_json() or request.form
        full_name = data['full_name']
        email = data['email']
        cpf = data['cpf']
        user.full_name = full_name
        user.email = email
        user.cpf = cpf
        db.session.commit()
        if request.get_json():
            return jsonify(user_schema.dump(user))
        elif request.form:
            return redirect(url_for('users.user_info', id=id))

    return render_template('users/edit_user.html', user=user)