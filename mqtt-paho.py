import paho.mqtt.client as mqtt
import time

# on_connect callback function called when CONNACK received from broker
def on_connect(client, userdata, flags, rc):
	print("Connected with result code"+ " " +str(rc))
  
# on_message callback function called when a PUBLISH message received from broker 
def on_message(client, userdata, message):
	print("'Received message ' "+ str(message.payload) + " ' on topic ' " + message.topic + "' with qos '" + str(message.qos))

#on_subscribe callback function called when SUBACK received from broker
def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribe_ack: " + str(mid) + " " + str(granted_qos))

# on_publish callback function called when PUBACK received from broker
def on_publish(client, userdata, mid):
	print("Publish_ack: " + str(mid))

broker_address = "iot.eclipse.org"
client = mqtt.Client("temp sensor")

# initialize callback functions
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# connect with broker, default_port=1883, keepalive =60 sec 
client.connect(broker_address, 1883, 60)

# PUBLISH a topic to broker with qos=1, retain=True
client.publish("/plano/temperature/", "100 Degree Celsius", 1, True)
client.publish("/plano/humidity/", "70%", 1, True)
#print("Publish rc: " + str(rc))

# start loop
client.loop_start()
client.subscribe("/plano/#")
time.sleep(5)
client.loop_stop()
