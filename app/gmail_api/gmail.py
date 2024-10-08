import re
import os

from simplegmail import Gmail
from simplegmail.query import construct_query

"""
The Gmail API is a RESTful API that can be used to access Gmail mailboxes and send mail.

This function connects to a Gmail account using credentials stored in a JSON file <client_secret.json>
to retrieve/extract a 6-digit verification code from emails in a Gmail account.
"""
def get_email_code():
    # Define the path to the Gmail API credentials file.
    # if running the script from the main directory (e.g., 'mexc_autotrading/run.py'):
    path = os.path.join(os.path.abspath("app\gmail_api\gmail_token.json"))

    # if running the script from within the 'app/gmail_api' directory.
    # path = os.path.join(os.path.abspath("gmail_token.json"))

    gmail = Gmail(creds_file=path)
    
    # contructs a query
    query_params = {
        "newer_than": (1, "hours"),
        "unread": True,
    }
    
    messages = gmail.get_messages(query=construct_query(query_params))
    
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)
        print("----------------------------")

        # marked as read after retrieving the message
        message.mark_as_read()
        
        if message.sender == "MEXC <dontreply@notification.mexc.link>" and message.subject == "[MEXC] Mã xác minh":
            # extract numbers from message.snippet
            nums_list = re.findall(r'\b\d+\b', message.snippet)
            code = None 
            for num in nums_list:
                if len(num) == 6:
                    code = num
            print(
                "------------------------------\n"
                f"Function <get_email_code> at gmail.py executed successfully. Code=<{code}>\n"
                "------------------------------\n"
                )
            return code
