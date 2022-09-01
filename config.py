import os

from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        self.EVERNOTE_CONSUMER_KEY = os.environ.get('EVERNOTE_CONSUMER_KEY')
        self.EVERNOTE_CONSUMER_SECRET = os.environ.get('EVERNOTE_CONSUMER_SECRET')
        self.EVERNOTE_PERSONAL_TOKEN = os.environ.get('EVERNOTE_PERSONAL_TOKEN')
        self.JOURNAL_TEMPLATE_NOTE_GUID = os.environ.get('JOURNAL_TEMPLATE_NOTE_GUID')
        self.JOURNAL_NOTEBOOK_GUID = os.environ.get('JOURNAL_NOTEBOOK_GUID')
        self.INBOX_NOTEBOOK_GUID = os.environ.get('INBOX_NOTEBOOK_GUID')
