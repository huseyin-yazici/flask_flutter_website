import firebase_admin
from firebase_admin import credentials, firestore

# Use the service account JSON file for credentials
cred = credentials.Certificate('/Users/huseyinyazici/Desktop/my_project/backend/flask_api/config/books-voyage-firebase-adminsdk-862cm-fa85d89b5a.json')
firebase_admin.initialize_app(cred)

db = firestore.client()