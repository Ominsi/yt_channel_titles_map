from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
import pickle
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def youtube_authenticate():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    config_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, "config/"))
    token_file = os.path.join(config_dir, 'token.pickle')
    client_secrets_file = os.path.join(config_dir, 'credentials.json')
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # sae the credentials for the next run
        with open(token_file, "wb") as token:
            pickle.dump(creds, token)

    return build(api_service_name, api_version, credentials=creds)
