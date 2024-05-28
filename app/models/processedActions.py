from app import db

class ProcessedAction(db.Model):
    __tablename__ = 'processed_action'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    session_id = db.Column(db.String(255), db.ForeignKey('session.id'))
    customer_id = db.Column(db.String(255), db.ForeignKey('customer.id'))
    action_id = db.Column(db.String(255), db.ForeignKey('action.id'))
    plan_id = db.Column(db.String(255), db.ForeignKey('company_plan.id'))
    conversation_id = db.Column(db.String(255), db.ForeignKey('conversation.id'))
    message_id = db.Column(db.String(255))
    action_type = db.Column(db.Enum())
    status = db.Column(db.Boolean)
    action_response = db.Column(db.JSON)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    action = db.relationship("actions", back_populates="processed_actions")
    customer = db.relationship("customers", back_populates="processed_actions")
    plan = db.relationship("company_plan", back_populates="processed_actions")
    session = db.relationship("sessions", back_populates="processed_actions")
    conversation = db.relationship("conversations", back_populates="processed_actions")
