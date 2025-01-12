HiveMQ Cloud provides a free MQTT broker for secure and reliable communication.
first Registered for a HiveMQ Cloud Free Plan on their website.
second Created a cluster, which will generated the following details:
      URL: 90b5426543625434723527532354235286480.s1.eu.hivemq.cloud
      Port (TLS): 8883
      Username: sam01
      Password: *********

you can now try to Opened the HiveMQ WebSocket Client in a web browser
and subscribe to a topic (test/topic) and successfully published and received messages.

MQTT Commands in Terminal:

installing mosquitto on mac :

Mosquitto is an MQTT broker and client package that includes tools for subscribing (mosquitto_sub) and publishing (mosquitto_pub) MQTT messages.


brew install mosquitto

to verify installation :   

mosquitto_sub --help

Use mosquitto_sub to subscribe to a topic:

mosquitto_sub -h 90b576576575757587587575cb6480.s1.eu.hivemq.cloud -p 8883 -u ‘sam01’ -P '**********' -t ‘test/topic’ --cafile /etc/ssl/cert.pem


Used mosquitto_pub to publish a message:

mosquitto_pub -h 90b7876876667756465476575480.s1.eu.hivemq.cloud -p 8883 -u ‘sam01’ -P '***********' -t ‘test/topic’ -m ‘Hello from macOS Terminal’ --cafile /etc/ssl/cert.pem

(((CA File: /etc/ssl/cert.pem (default location for trusted certificates on macOS).)))


install then any phone app like IotMqttPanel where you can also send and receive mqtt messages 

load the script main_back.py to esp32 and rename it to main.py : you will be able to control
the onboard led from you phone app and from esp32 to send message to the phone app by pressing
the en onboard button from anywhere when connected to internet


