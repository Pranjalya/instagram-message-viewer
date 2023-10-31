import os
import json
from glob import glob
from models import *
from pprint import pprint

user = ""
msgs = []

for message_json in glob(f"data/messages/inbox/{user}/message_*.json"):
    with open(message_json) as f:
        data = json.load(f)
    msgs.extend(data["messages"])

parsed = parse_messages(msgs)
pprint(parsed)
