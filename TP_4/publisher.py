import paho.mqtt.client as mqtt
import random
import time

# Create MQTT client instance with callback API v2
client = mqtt.Client(
    client_id="Capteur", callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

broker_address = "localhost"
client.connect(broker_address)  # Connect to broker

while True:
    temperature = random.uniform(20.0, 25.0)  # Generate random temperature
    # Convert temperature to string before publishing
    client.publish("maison/salon/temperature", str(temperature))  # Publish to topic
    print(f"Published temperature: {temperature}")  # Optional: print for debugging
    time.sleep(5)  # Wait 5 seconds before next reading
