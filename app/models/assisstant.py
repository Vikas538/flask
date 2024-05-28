from app import db
from enums.enums import AssistantTypeEnum, LLMSEnum

class Assistant(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    company_id = db.Column(db.String)
    plan_id = db.Column(db.String)
    kb_id = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    type = db.Column(db.Enum(AssistantTypeEnum))
    application_id = db.Column(db.String)
    synthesizer = db.Column(db.String)
    enable_recordings = db.Column(db.Boolean)
    status = db.Column(db.Boolean)
    api_key = db.Column(db.String)
    api_secret = db.Column(db.String)
    intents = db.Column(db.ARRAY(db.String))
    entities = db.Column(db.ARRAY(db.String))
    keys = db.Column(db.JSON)
    capabilities = db.Column(db.String)
    jwt = db.Column(db.String)
    incoming_call_greeting = db.Column(db.String)
    outgoing_call_greeting = db.Column(db.String)
    notes = db.Column(db.JSON)
    project_details = db.Column(db.JSON)
    instructions = db.Column(db.JSON)
    ap_api_key = db.Column(db.String)
    prompts = db.Column(db.JSON)
    ai_type = db.Column(db.Enum(LLMSEnum))
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    created_by = db.Column(db.String)
    updated_by = db.Column(db.String)

    user_plan = db.relationship('Company_plan', backref=db.backref('assistants', lazy=True))
    kb = db.relationship('KnowledgeBase', backref=db.backref('assistants', lazy=True))
    session = db.relationship('Session', backref=db.backref('assistant', lazy=True))
