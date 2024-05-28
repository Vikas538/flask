from app import db

class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    slug = db.Column(db.String(255))
    company_id = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    workspace_role = db.relationship("role_permission_map", backref=db.backref("user_role", cascade="all, delete-orphan"))
    company = db.relationship("company", backref=db.backref("user_role", cascade="all, delete-orphan"))
    user = db.relationship("user", backref=db.backref("user_role", cascade="all, delete-orphan"))
