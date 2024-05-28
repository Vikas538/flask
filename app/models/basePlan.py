from app import db
from enums.enums import AssistantTypeEnum, LLMSEnum
class BasePlan(db.Model):
    __tablename__ = 'base_plan'

    id = db.Column(db.String, primary_key=True, unique=True, default=db.func.cuid())
    plan_name = db.Column(db.String)
    plan_type = db.Column(db.String)  # Adjust data type if necessary
    module_profile_id = db.Column(db.Integer, db.ForeignKey('module_profile.id'))
    no_of_emails_per_day = db.Column(db.Integer)
    no_of_emails_per_month = db.Column(db.Integer)
    no_of_minutes_per_day = db.Column(db.Integer)
    no_of_calls_per_month = db.Column(db.Integer)
    llms = db.Column(db.ARRAY(LLMSEnum))
    max_allowed_token = db.Column(db.Integer)
    max_number_of_kb = db.Column(db.Integer)
    max_number_of_action = db.Column(db.Integer)
    assistants_daily_budget = db.Column(db.JSON)
    max_no_assistants = db.Column(db.Integer)
    price = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_plan = db.relationship('company_plan', backref='base_plan', lazy=True)
    module_profile = db.relationship('module_profile', backref='base_plan', lazy=True)
