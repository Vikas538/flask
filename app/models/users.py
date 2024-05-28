from app import db
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False, default=db.func.cuid())
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone = db.Column(db.String)
    status = db.Column(db.Enum('ACTIVE', 'PAUSED', 'OTHER', name='user_status'))
    user_role_id = db.Column(db.Integer, unique=True)
    notes = db.Column(db.JSON)
    company_id = db.Column(db.String, nullable=False)
    department = db.Column(db.Enum('USER', 'COMPANY', 'OTHER', name='department'))
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    created_by = db.Column(db.String)
    updated_by = db.Column(db.String)

    company = db.relationship('Company', backref=db.backref('users', lazy=True))
    user_role = db.relationship('UserRole', backref=db.backref('user', lazy=True))
    user_meta_data = db.relationship('UserMetaData', backref=db.backref('user', lazy=True))
    note = db.relationship('Note', backref=db.backref('user', lazy=True))