from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    workload_per_week = db.Column(db.Integer, nullable=False, default=16)
    is_admin = db.Column(db.Boolean, default=False)  # Admin flag
    is_approved = db.Column(db.Boolean, default=False)  # Approval status

class ClassDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dairy_no = db.Column(db.Integer, unique=True, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    subject_code = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    actual_hours = db.Column(db.Integer, nullable=False)
    claiming_hours = db.Column(db.Integer, nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)