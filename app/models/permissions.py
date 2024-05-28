from app import db

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    slug = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    workspace_role_permission = db.relationship("role_permission_map", backref=db.backref("permission", cascade="all, delete-orphan"))
