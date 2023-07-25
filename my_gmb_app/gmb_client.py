# my_gmb_app/gmb_client.py
import google.oauth2.credentials
from google.auth.transport.requests import Request
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

# Define the GMB scopes you need
SCOPES = ['https://www.googleapis.com/auth/business.manage']

def get_gmb_service():
    # Load or create GMB credentials
    creds_file = 'credentials.pickle'
    if os.path.exists(creds_file):
        with open(creds_file, 'rb') as token:
            creds = pickle.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret_1019557246053-dnftdv27j1hmfsiafpfov0k4tb63i1g4.apps.googleusercontent.com.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open(creds_file, 'wb') as token:
            pickle.dump(creds, token)

    # Build the GMB service
    service = build('mybusiness', 'v4', credentials=creds)
    return service
