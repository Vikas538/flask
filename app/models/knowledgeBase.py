from app import db

class knowledge_base(db.Model):
    __tablename__ = 'knowledge_base'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    name = db.Column(db.String(255))
    company_id = db.Column(db.String(255), db.ForeignKey('company.id'))
    user_plan_id = db.Column(db.String(255), db.ForeignKey('company_plan.id'))
    status = db.Column(db.Boolean)
    files = db.Column(db.JSON)
    urls = db.Column(db.JSON)
    faqs = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    company = db.relationship("company", back_populates="knowledge_base")
    user_plan = db.relationship("company_plan", back_populates="knowledge_base", foreign_keys=[user_plan_id])
    assistants = db.relationship("assistants", back_populates="knowledge_base")
