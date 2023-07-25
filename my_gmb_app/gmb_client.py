from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from my_gmb_project.settings import *
def get_gmb_service():
    credentials = Credentials(
        token=GMB_ACCESS_TOKEN,
        refresh_token=GMB_REFRESH_TOKEN,
        client_id=GMB_CLIENT_ID,
        client_secret=GMB_CLIENT_SECRET
    )

    return build('mybusiness', 'v4', credentials=credentials)
