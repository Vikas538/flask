from app import db
from enums.enums import AssistantTypeEnum, LLMSEnum
class ApiKey(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    api_type = db.Column(db.Enum(LLMSEnum))
    company_id = db.Column(db.String, nullable=False)
    customer_key = db.Column(db.String)
    api_key = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    company = db.relationship('Company', backref=db.backref('api_keys', lazy=True))