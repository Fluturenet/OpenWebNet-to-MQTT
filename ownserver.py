import paho.mqtt.client as mqtt
import time
import socket


broker_address="core-mosquitto"

gateway_addr_port = "local-openwebnet",20000

def on_message(client,userdata,message):
    payload=str(message.payload.decode("utf-8"))
    topic=message.topic.split("/")
    if(len(topic)!=4):
        print("Error: ",message.topic)
        return
    if (topic[2]=="cover"):
        who="2"
        what="0"
        where=topic[3]
        if (payload=="OPEN"): what="1"
        if (payload=="CLOSE"): what="2"
        send_message('*'+who+'*'+what+'*'+where+"##")


def send_message(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(gateway_addr_port)
    sock.send(msg)
    return


client = mqtt.Client("bticino") #create new instance
client.on_message=on_message #attach function to callback

client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

client.subscribe("bticino/#")

while (1):
    time.sleep(5)
