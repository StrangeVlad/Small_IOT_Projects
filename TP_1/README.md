# 📡 LoRaWAN Communication for Sensor Data Transmission

This project sets up a **LoRaWAN communication system** to send temperature data from a sensor node to a gateway. It includes both:

1. **Real LoRa Communication** using the PyLoRa library.
2. **Simulated Version** for testing on a PC without LoRa hardware.

---

## **🔹 What is LoRaWAN?**

LoRaWAN (Long Range Wide Area Network) is a **low-power wireless communication protocol** used in IoT (Internet of Things). It allows devices to send **small amounts of data over long distances** (up to 10 km).

### **✅ Why Use LoRaWAN?**

- **Long Range** → Covers several kilometers.
- **Low Power** → Devices can run for **years** on batteries.
- **Low Cost** → No need for SIM cards or expensive networks.
- **Ideal for IoT** → Used in **smart agriculture, weather stations, and industrial automation**.

---

## **📦 Requirements**

- **LoRa Module** (e.g., RFM95)
- **Python 3** installed
- **PyLoRa Library**

---

## **📌 Installation**

Before running the script, install the **PyLoRa** library:

```bash
pip install lora
```

## Real LoRaWAN Communication Code

If you have a real LoRa module, use the following Python script:

```python
from lora import LoRa
import random
import time

# Initialize LoRa Module
lora = LoRa()
lora.set_mode(Lora.MODE.STDBY)

# Configure LoRa Parameters
lora.set_frequency(868.1)  # Frequency in MHz
lora.set_tx_power(14)      # Transmission power (14 dBm)
lora.set_bandwidth(125)    # Bandwidth in kHz
lora.set_spreading_factor(7) # Controls range vs. speed
lora.set_coding_rate(5)    # Error correction settings

print("LoRa module initialized.")
print(f"Configured parameters: frequency = 868.1 MHz, TX power = 14 dBm, bandwidth = 125 kHz, spreading factor = 7, coding rate = 5.\n")

# Send data continuously
while True:
    temperature = round(random.uniform(20.0, 25.0), 1)  # Generate random temperature
    print(f"Sending data: {temperature}")
    lora.send(str(temperature))  # Send data
    print("Data sent successfully.")
    print("Pausing for 60 seconds...\n")
    time.sleep(60)  # Wait 60 seconds before sending again
```

## 🔍 Code Explanation

### Step Description

1. Install the lora library.
2. Import LoRa, random, and time.
3. Initialize LoRa module and set it to standby mode.
4. Configure frequency, transmission power, bandwidth, spreading factor, and coding rate.
5. Generate a random temperature value between 20°C and 25°C.
6. Send the temperature data over LoRa every 60 seconds.
7. Display a confirmation message after sending each data packet.
   🖥️ Simulated Version (No Hardware Needed)
   If you don’t have a LoRa module, you can run this simulation to test the functionality:

```python
import random
import time

# Function to simulate sending data over LoRa

def simulate_lora_send(data):
print(f"Sending data: {data}")
time.sleep(1) # Simulate transmission delay
print("Data sent successfully.")
print("Pausing for 60 seconds...\n")

# Function to generate random temperature

def read_temperature():
return round(random.uniform(20.0, 25.0), 1)

# Run simulation in a loop

while True:
temperature = read_temperature() # Get random temperature
simulate_lora_send(temperature) # Simulate sending data
time.sleep(60) # Wait 60 seconds before sending again
```

## 📝 Expected Output

When running either script, you should see:

```python
LoRa module initialized.
Configured parameters: frequency = 868.1 MHz, TX power = 14 dBm, bandwidth = 125 kHz, spreading factor = 7, coding rate = 5.

Sending data: 22.5
Data sent successfully.
Pausing for 60 seconds...

Sending data: 23.1
Data sent successfully.
Pausing for 60 seconds...

Sending data: 21.9
Data sent successfully.
Pausing for 60 seconds...
```

## 🌍 Real-World Applications

- Smart Agriculture: Monitoring temperature, humidity, soil moisture.
- Smart Cities: Detecting air quality, traffic flow.
- Industrial IoT: Monitoring machine health and energy usage.
- Remote Monitoring: Sending sensor data from remote areas.

## 📢 Conclusion

This project demonstrates how to use LoRaWAN for IoT sensor data transmission. If you don’t have a LoRa module, you can simulate the functionality using Python.
