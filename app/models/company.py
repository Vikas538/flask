from app import db

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.String, primary_key=True, unique=True, default=db.func.cuid())
    company_name = db.Column(db.String)
    customer_name = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    website = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)
    zip_code = db.Column(db.String)
    customer_type = db.Column(db.String)  # Adjust data type if necessary
    industry = db.Column(db.String)  # Adjust data type if necessary
    subIndustry = db.Column(db.String)  # Adjust data type if necessary
    department = db.Column(db.String)  # Adjust data type if necessary
    subDepartment = db.Column(db.String)  # Adjust data type if necessary
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_plan = db.relationship('CompanyPlan', backref='company', lazy=True)
    notes = db.Column(db.JSON)
    fields = db.Column(db.JSON)
    knowledge_base = db.relationship('KnowledgeBase', backref='company', lazy=True)
    customers = db.relationship('Customer', backref='company', lazy=True)
    api_key = db.relationship('ApiKey', backref='company', lazy=True)
    user_roles = db.relationship('UserRole', backref='company', lazy=True)
    users = db.relationship('User', backref='company', lazy=True)
    actions = db.relationship('Action', backref='company', lazy=True)
    training_data = db.relationship('TrainingData', backref='company', lazy=True)
    email_templates = db.relationship('EmailTemplate', backref='company', lazy=True)
