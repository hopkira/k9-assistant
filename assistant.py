

import json
import sys
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

sys.path.append('..')  # persistent import directory for K9 secrets

from k9secrets import IAMAuthenticatorKey, assistant_service_URL, assistant_id

authenticator = IAMAuthenticator(IAMAuthenticatorKey)
assistant = AssistantV2(
    version='2020-04-01',
    authenticator=authenticator)
assistant.set_service_url(assistant_service_URL)

#########################
# Sessions
#########################

session = assistant.create_session(assistant_id).get_result()
print("Session established")

#########################
# Message
#########################

message = assistant.message(
    assistant_id,
    session["session_id"],
    input={'text': 'What is your purpose?'},
    context={
        'metadata': {
            'deployment': 'myDeployment'
        }
    }).get_result()

text = message["output"]["generic"][0]["text"]

print(text)
#print(json.dumps(message, indent=2))

assistant.delete_session(assistant_id, session["session_id"]).get_result()