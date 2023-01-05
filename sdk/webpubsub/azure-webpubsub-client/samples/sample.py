import os
import time
import json
from azure.webpubsub.client import WebPubSubClient, WebPubSubClientCredential
from azure.messaging.webpubsubservice import WebPubSubServiceClient
from azure.webpubsub.client import OnConnectedArgs, SendToGroupOptions, WebPubSubClientOptions, OnGroupDataMessageArgs
from dotenv import load_dotenv

load_dotenv()


def on_connected(connected: OnConnectedArgs):
    print("===================")
    print(connected)

def on_group_message(message: OnGroupDataMessageArgs):
    print(message.message)

# def on_close()
service_client = WebPubSubServiceClient.from_connection_string(
    connection_string=os.getenv("WEBPUBSUB_CONNECTION_STRING"), hub="Hub"
)

url = service_client.get_client_access_token(roles=["webpubsub.joinLeaveGroup", "webpubsub.sendToGroup"])["url"]
print(url)

client = WebPubSubClient(client_access_url=url, options=WebPubSubClientOptions(auto_reconnect=False))
client.start()
client.join_group("test")
count = 0
while True:
    count = count + 1
    client.send_to_group(
        group_name="test",
        content=str(count),
        data_type="text",
        options=SendToGroupOptions(no_echo=False, fire_and_forget=True),
    )
    print(count)
    time.sleep(5)