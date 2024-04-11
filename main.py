from fastapi import FastAPI
import json

from models import ContactsTable, FromClient, FromUser
from mongoengine import connect
import csv
from io import StringIO
connect('contacts', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/contacts")
app = FastAPI()


@app.post("/v1/api/add-bde-contact")
async def addBdeContact(body: FromUser):
    saveContact = ContactsTable(appName = body.appName, username = body.username, contactname = body.contactname, phone = body.phone, countryCode = body.countryCode, email=body.email )
    saveContact.save()
    return {
        "message":"Done",
    }
    
@app.post("/v1/api/add-from-client-contact")
async def addClientContact(body: FromClient):
    saveContact = ContactsTable(appName = body.appName, clientName = body.clientName, contactname = body.contactname, phone = body.phone, countryCode = body.countryCode, email=body.email )
    saveContact.save()
    return {
        "message":"Done",
    }
    
@app.get("/find/data-by-email-contacts/{email}")
async def findata(email: str):
    findData = ContactsTable.objects(email=email)
    if findData:
        # Prepare data for CSV conversion
        data = [
            (contact.appName, contact.contactname, contact.phone, contact.email, contact.countryCode)
            for contact in findData
        ]
        # Convert data to CSV format
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        # Write headers
        csv_writer.writerow(["AppName", "ContactName", "Phone", "Email", "CountryCode"])
        # Write rows
        csv_writer.writerows(data)
        # Move to the beginning of the buffer
        csv_data.seek(0)
        return csv_data.getvalue(), 200, {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment; filename="contacts.csv"'}
    else:
        return {
            "message": "Contacts not found",
            "status": False
        }
    