### Solution to MQTT Exercise

## Part A: Description of MQTT

# Description of MQTT:

MQTT (Message Queuing Telemetry Transport) is a lightweight publish/subscribe messaging protocol designed for low-bandwidth, high-latency, or unreliable networks. It's ideal for IoT applications where devices need to communicate efficiently with minimal overhead.

# Advantages of MQTT:

Lightweight and simple: Minimal protocol overhead, making it perfect for IoT devices with limited resources
Reliable delivery: Offers three Quality of Service (QoS) levels for guaranteed message delivery
Publish/Subscribe model: Decouples senders and receivers, allowing flexible communication patterns
Bi-directional communication: Devices can both send and receive messages easily
Low power consumption: Ideal for battery-powered devices
Security support: Supports SSL/TLS encryption and authentication

# Uses of MQTT:

IoT sensor networks (temperature, humidity monitoring)
Home automation systems
Industrial IoT and monitoring systems
Mobile messaging applications
Remote monitoring and control systems
Smart city infrastructure

## Part B: MQTT Messaging System Implementation

# Complete Solution for Sensor Script (publisher):

```
import paho.mqtt.client as mqtt
import random
import time

broker_address = "localhost"
client = mqtt.Client("Capteur") # Create MQTT client instance
client.connect(broker_address) # Connect to broker

while True:
temperature = random.uniform(20.0, 25.0) # Generate random temperature
client.publish("maison/salon/temperature", temperature) # Publish to topic
time.sleep(5) # Wait 5 seconds before next reading
```

# Complete Solution for Subscriber Script:

```
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
print(f"Message reçu: {message.payload.decode()}")

broker_address = "localhost"
client = mqtt.Client("passerelle") # Create client instance
client.connect(broker_address) # Connect to broker

client.on_message = on_message # Attach callback function
client.subscribe("maison/salon/temperature") # Subscribe to topic
client.loop_forever() # Start network loop
```

# The code snippet from the first image is partially incomplete and out of order. Here's what it should do when properly organized:

- client-subscribe("maison/salon/temperature") - This line has a syntax error (should be client.subscribe)
- client.on_message = on_message - This assigns a callback function for received messages
- client.loop_forever() - This starts the network loop to handle network traffic
- The following lines create and connect a client (should be before the above operations)

Results when properly organized:

Creates a client named "passerelle"
Connects to the localhost broker
Subscribes to the temperature topic
Continuously waits for messages and prints them when received

The code will run indefinitely, displaying any temperature messages published to the "maison/salon/temperature" topic.
Implementation Steps:

Install MQTT broker (Mosquitto):
bashsudo apt-get install mosquitto mosquitto-clients

Start the MQTT broker:
bashsudo systemctl start mosquitto

Run the sensor script (publisher) which generates random temperature values and publishes them
Run the subscriber script which receives and displays the temperature readings

The system will continuously send temperature data from the sensor to the gateway through the MQTT broker.

pip install paho-mqtt
download and install mosquito 'https://mosquitto.org/download/'
