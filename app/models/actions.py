from app import db
class Action(db.Model):
    __tablename__ = 'action'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False, default=db.func.cuid())
    company_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    type = db.Column(db.Enum('EMAIL', 'SMS', 'WEBHOOK', 'OTHER', name='processed_action_type'))
    email = db.Column(db.String)
    sms = db.Column(db.String)
    webhook = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    company = db.relationship('Company', backref=db.backref('actions', lazy=True))
    processed_actions = db.relationship('ProcessedAction', backref=db.backref('action', lazy=True))
