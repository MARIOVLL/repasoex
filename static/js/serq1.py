import paho.mqtt.client as mqtt
import time
def on_message(client, obj, msg):
print(msg.topic + " " + str(msg.qos) + " " + msg.payload)
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set("veintimillamario035@gmail.com","12345678")
mqttc.connect("maqiatto.com", 1883)
mqttc.subscribe("veintimillamario035@gmail.com/test", 0)
rc=0
print("inicio...")
while rc == 0:
 time.sleep(2)
 rc = mqttc.loop()
 mqttc.publish("veintimillamario035@gmail.com/test",0)