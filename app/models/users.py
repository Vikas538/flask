from app import db
from .enums.enums import DepartmentEnum,UserStatusEnum
class user(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False, default=db.func.cuid())
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone = db.Column(db.String)
    status = db.Column(db.Enum(UserStatusEnum,name='UserStatusEnum'))
    user_role_id = db.Column(db.Integer, unique=True)
    notes = db.Column(db.JSON)
    company_id = db.Column(db.String, nullable=False)
    department = db.Column(db.Enum(DepartmentEnum,name='UserStatusEnum'))
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    created_by = db.Column(db.String)
    updated_by = db.Column(db.String)

    company = db.relationship('company', backref=db.backref('user', lazy=True))
    user_role = db.relationship('user_role', backref=db.backref('user', lazy=True))
    user_meta_data = db.relationship('user_meta_data', backref=db.backref('user', lazy=True))
    note = db.relationship('note', backref=db.backref('user', lazy=True))