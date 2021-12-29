import sys

sys.path.append('/home/devuser/leedbot')
from dbapi.dbapi import DatabaseAPI
from bot.utils.misc.formatm import get_data
import imaplib, email
from email.header import decode_header
import re
import time

def get_text(msg):
    if msg.is_multipart():
        return get_text(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


def format_text(text):
    return text.decode('utf-8').replace('\r', '')


def write_to_db(message, db):
    db.upload(db.oper_queue, {'ids': db.generate_objectid(),
                         'message': message,
                         'source': 1,
                         'inwork': False,
                         'status': 'none'})
    print('writed')
def get_message(response, db):
    if isinstance(response, tuple):
        msg = email.message_from_bytes(response[1])
        print(get_text(msg).decode('utf-8'))
        write_to_db(get_text(msg).decode('utf-8'), db)


def get_all_messages(imap):
    return imap.select('INBOX')


def read_email_from_gmail(imap, db, n):
    try:
        status, messages = get_all_messages(imap)
        for i in range(int(messages[0]), int(messages[0])-n, -1):
          res, msg = imap.fetch(str(i), "(RFC822)")
          for response in msg:
              get_message(response, db)
    except Exception as ex:
        print(ex)


imap = imaplib.IMAP4_SSL('imap.gmail.com')
imap.login("gornyjivan1@gmail.com", "X0uDwI|jzPVsSpW$")
messages = int(get_all_messages(imap)[1][0])
db = DatabaseAPI()

while True:
    check_messages = int(get_all_messages(imap)[1][0])
    new_messages = check_messages - messages
    if new_messages > 0:
        print('new message here')
        read_email_from_gmail(imap, db, new_messages)
        messages = check_messages
