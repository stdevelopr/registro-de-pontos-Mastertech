# from . import db
from . import db, ma
from flask_marshmallow import fields

class User(db.Model):
    """Data model for user accounts."""
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    full_name = db.Column(
        db.String(200),
        index=False,
        nullable=False
    )

    email = db.Column(
        db.String(80),
        index=False,
        nullable=True
    )

    cpf = db.Column(
        db.String(80),
        index=False,
        unique=True,
        nullable=True
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.full_name)


class UserSchema(ma.Schema):
    class Meta:
       model = User
       fields = ('id', 'full_name', 'email', 'cpf')


class Clock(db.Model):
    """Data model for clock punchs."""
    __tablename__ = 'clock'
    __table_args__ = {'extend_existing': True}

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        index=True,
        nullable=False
    )

    time = db.Column(
        db.DateTime,
        nullable=False
    )

    exit_type = db.Column(
        db.Boolean,
        nullable=False
    )

class ClockSchema(ma.Schema):
    class Meta:
       fields = ('user_id', 'time', 'exit_type')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
clock_schema = ClockSchema()
clock_punches_schema = ClockSchema(many=True)