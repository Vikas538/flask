from app import db
from enums.enums import RequestTypeEnum

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    method = db.Column(db.Enum(RequestTypeEnum))
    url = db.Column(db.String)
    headers = db.Column(db.JSON)
    query_params = db.Column(db.JSON)
    body_params = db.Column(db.JSON)
    details = db.Column(db.JSON)
    response_code = db.Column(db.Integer)
    user_meta_data_id = db.Column(db.Integer, db.ForeignKey('user_meta_data.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    user_meta_data = db.relationship('UserMetaData', backref=db.backref('requests', lazy=True))
