from app import db
from enums.enums import InvoiceStatusEnum, PaymentModeEnum, PlanTypeEnum
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    paymentStatus = db.Column(db.Enum(InvoiceStatusEnum))
    plan_id = db.Column(db.String)
    paymentMode = db.Column(db.Enum(PaymentModeEnum))
    amountPaid = db.Column(db.Float)
    invoice_created_at = db.Column(db.DateTime)
    payment_date = db.Column(db.DateTime)
    last_payment_date = db.Column(db.DateTime)
    invoiceType = db.Column(db.Enum(PlanTypeEnum))
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    user_plan = db.relationship('Company_plan', backref=db.backref('invoices', lazy=True))