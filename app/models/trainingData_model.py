from app import db

class TrainingData(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    company_id = db.Column(db.String(36), nullable=False)
    fags = db.Column(db.JSON)
    model = db.Column(db.Enum("CHATGPT_4_0", "LLAMA3", "OTHER"))
    trained_data = db.Column(db.JSON)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    company = db.relationship('Company', backref=db.backref('training_data', lazy=True))
