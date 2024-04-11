from mongoengine import Document, StringField
from pydantic import BaseModel
class ContactsTable(Document):
    appName = StringField(required=True)
    username = StringField(required=False)
    clientName = StringField(required=False)
    contactname = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    countryCode = StringField(required=True)
    
class FromUser(BaseModel):
    appName: str
    username: str
    contactname: str
    phone: str
    email: str
    countryCode: str
    
class FromClient(BaseModel):
    appName: str
    clientName: str
    phone: str
    contactname: str
    email: str
    countryCode: str