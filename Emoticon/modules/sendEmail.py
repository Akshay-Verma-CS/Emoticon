from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64
import os
import pickle

class GmailSender:
    APP_PATH = os.getcwd() + "/Emoticon/configuration/"
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    CREDENTIALS_FILE = APP_PATH + 'credentials.json'
    print(f"credentials file path  - {CREDENTIALS_FILE}")
    TOKEN_FILE = APP_PATH + 'token.pickle'

    def __init__(self):
        """Initializes GmailSender and authenticates using saved token or credentials file."""
        creds = None
        # Load credentials from the token file.
        if os.path.exists(self.TOKEN_FILE):
            with open(self.TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIALS_FILE, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('gmail', 'v1', credentials=creds)

    def create_message(self, sender, to, subject, message_text):
        """Creates a message for an email."""
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': encoded_message}

    def send_message(self, user_id, message):
        """Send an email message."""
        try:
            sent_message = (self.service.users().messages().send(userId=user_id, body=message)
                            .execute())
            print('Message Id: %s' % sent_message['id'])
            return sent_message
        except Exception as error:
            print('An error occurred: %s' % error)

# if __name__ == '__main__':
#     gmail_sender = GmailSender()
#     sender_email = "aarshmail@gmail.com"
#     receiver_email = "topensite@gmail.com"
#     subject = "Test Subject"
#     body = "Hello, this is a test email."
#     message = gmail_sender.create_message(sender_email, receiver_email, subject, body)
#     gmail_sender.send_message("me", message)
# print(os.getcwd())