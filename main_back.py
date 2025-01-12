import network
import time
import machine
from umqtt.simple import MQTTClient

# Wi-Fi credentials
WIFI_SSID = "Rassi Net3"
WIFI_PASSWORD = "*********"

# MQTT configuration
MQTT_BROKER = "90d3354535435435435345fg45345cb6480.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USER = "sam02"
MQTT_PASSWORD = "Hol******7"
MQTT_TOPIC_SUBSCRIBE = "test/topic"
MQTT_TOPIC_PUBLISH = "test/gpio"

# GPIO configuration
BUTTON_PIN = 0  # EN button (GPIO 0 on ESP32-S2)
LED_PIN = 2  # Onboard LED (GPIO 2)

# Function to connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    print("Connecting to WiFi...", end="")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nWiFi connected! IP:", wlan.ifconfig()[0])

# Callback function for received messages
def mqtt_message_callback(topic, msg):
    print(f"Message received on topic {topic.decode('utf-8')}: {msg.decode('utf-8')}")
    if topic.decode('utf-8') == MQTT_TOPIC_SUBSCRIBE:
        if msg.decode('utf-8').lower() == "on":
            led.value(1)  # Turn on LED
            print("LED turned ON")
        elif msg.decode('utf-8').lower() == "off":
            led.value(0)  # Turn off LED
            print("LED turned OFF")

# Main program
def main():
    connect_to_wifi()

    print("Connecting to MQTT broker...")
    try:
        client = MQTTClient(
            client_id="esp32_client",
            server=MQTT_BROKER,
            port=MQTT_PORT,
            user=MQTT_USER,
            password=MQTT_PASSWORD,
            ssl=True,
            ssl_params={'server_hostname':'90d3354535435435435345fg45345cb6480.s1.eu.hivemq.cloud'}  # certificate verification
        )
        client.set_callback(mqtt_message_callback)
        client.connect()
        print("MQTT connected!")
    except Exception as e:
        print(f"MQTT connection failed: {type(e).__name__}, {e}")
        return

    client.subscribe(MQTT_TOPIC_SUBSCRIBE)
    print(f"Subscribed to topic: {MQTT_TOPIC_SUBSCRIBE}")

    # Configure the button pin
    button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

    # Configure the LED pin
    global led
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    led.value(0)  # Ensure LED is off initially

    try:
        while True:
            # Check for messages from the subscribed topic
            client.check_msg()

            # Check if the button is pressed
            if not button.value():  # Button is active low
                print("Button pushed, publishing message...")
                client.publish(MQTT_TOPIC_PUBLISH, "button pushed")
                time.sleep(0.5)  # Debounce delay
    except KeyboardInterrupt:
        print("Disconnecting...")
        client.disconnect()
        print("Disconnected.")

if __name__ == "__main__":
    main()
