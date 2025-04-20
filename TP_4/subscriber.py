import paho.mqtt.client as mqtt


# Callback for API version 2
def on_message(client, userdata, msg):
    print(f"Message reçu: {msg.payload.decode()}")
    print(f"Topic: {msg.topic}")


# Create MQTT client instance with callback API v2
client = mqtt.Client(
    client_id="passerelle", callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

broker_address = "localhost"
client.connect(broker_address)

# Set the message callback
client.on_message = on_message

# Subscribe to the topic
client.subscribe("maison/salon/temperature")
print("Subscribed to maison/salon/temperature")

# Start the network loop
client.loop_forever()
