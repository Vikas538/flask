from app import db

class EmailTemplate(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False, default=db.func.uuid_generate_v4())
    company_id = db.Column(db.String(36), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    company = db.relationship('Company', backref=db.backref('email_templates', lazy=True))
    sent_emails = db.relationship('SentEmail', backref=db.backref('email_template', lazy=True))
