from app import db
from .enums.enums import IndustryEnum,DepartmentEnum,CustomerTypeEnum

class company(db.Model):
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
    customer_type = db.Column(db.Enum(CustomerTypeEnum,name='CustomerTypeEnum'))  # Adjust data type if necessary
    industry = db.Column(db.Enum(IndustryEnum,name='IndustryEnum'))  # Adjust data type if necessary
    subIndustry = db.Column(db.Enum(IndustryEnum,name='IndustryEnum'))  # Adjust data type if necessary
    department = db.Column(db.Enum(DepartmentEnum,name=DepartmentEnum))  # Adjust data type if necessary
    subDepartment = db.Column(db.Enum(DepartmentEnum,name='DepartmentEnum'))  # Adjust data type if necessary
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_plan = db.relationship('company_plan', backref='company', lazy=True)
    notes = db.Column(db.JSON)
    fields = db.Column(db.JSON)
    knowledge_base = db.relationship('knowledge_base', backref='company', lazy=True)
    customers = db.relationship('customers', backref='company', lazy=True)
    api_key = db.relationship('api_keys', backref='company', lazy=True)
    user_roles = db.relationship('user_role', backref='company', lazy=True)
    users = db.relationship('user', backref='company', lazy=True)
    actions = db.relationship('actions', backref='company', lazy=True)
    training_data = db.relationship('training_data', backref='company', lazy=True)
    email_templates = db.relationship('email_templates', backref='company', lazy=True)
