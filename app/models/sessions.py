from app import db

class Session(db.Model):
    __tablename__ = 'session'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    assistant_id = db.Column(db.Integer, db.ForeignKey('assistant.id'))
    from_ = db.Column(db.String(255))  # Renamed from 'from' to avoid keyword conflict
    to = db.Column(db.String(255))
    session_type = db.Column(db.String(255))
    direction = db.Column(db.String(255))
    medium = db.Column(db.String(255))
    customer_id = db.Column(db.String(255), db.ForeignKey('customer.id'))
    plan_id = db.Column(db.String(255), db.ForeignKey('company_plan.id'))
    conversations = db.Column(db.String(255))
    session_started_at = db.Column(db.DateTime)
    session_ended_at = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    session_cost = db.Column(db.Float)
    session_state = db.Column(db.String(255))
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    assistant = db.relationship("Assistant", back_populates="sessions")
    customer = db.relationship("Customer", back_populates="sessions")
    company_plan = db.relationship("CompanyPlan", back_populates="sessions")
    processed_actions = db.relationship("ProcessedAction", back_populates="session")
