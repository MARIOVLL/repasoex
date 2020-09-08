import paho.mqtt.client as mqtt
import time
def on_message(client, obj, msg):
	#print("hola_conectado")
	print(msg.topic + " " + str(msg.qos) + " " + msg.payload.decode("utf-8"))


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set("veintimillamario035@gmail.com","12345678")
mqttc.connect("maqiattO.com", 1883)
mqttc.subscribe("veintimillamario035@gmail.com/test1", 0)
rc=0
print("inicio...")
print("Mario_V")
i=0
while rc == 0:
	time.sleep(2)
	rc = mqttc.loop()
	mqttc.publish("veintimillamario035@gmail.com/test","sensor="+str(i)+"-"+str(i+1))
	i=i+1