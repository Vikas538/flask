from app import db

class WorkspaceRolePermission(db.Model):
    __tablename__ = 'role_permission_map'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    role_id = db.Column(db.Integer)
    permission_id = db.Column(db.Integer)
    
    permission = db.relationship("permissions", backref=db.backref("role_permission_map", cascade="all, delete-orphan"))
    role = db.relationship("user_role", backref=db.backref("role_permission_map", cascade="all, delete-orphan"))