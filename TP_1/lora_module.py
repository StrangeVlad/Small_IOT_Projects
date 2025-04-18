import random
import time


class LoRa:
    """A class to simulate LoRa functionality"""

    class MODE:
        SLEEP = 0
        STDBY = 1
        TX = 2
        RX = 3

    def __init__(self):
        self.mode = self.MODE.SLEEP
        self.frequency = 0
        self.tx_power = 0
        self.bandwidth = 0
        self.spreading_factor = 0
        self.coding_rate = 0
        print("Initializing LoRa module...")

    def set_mode(self, mode):
        self.mode = mode

    def set_frequency(self, freq):
        self.frequency = freq

    def set_tx_power(self, power):
        self.tx_power = power

    def set_bandwidth(self, bw):
        self.bandwidth = bw

    def set_spreading_factor(self, sf):
        self.spreading_factor = sf

    def set_coding_rate(self, cr):
        self.coding_rate = cr

    def send(self, data):
        """Simulate sending data via LoRa"""
        return simulate_lora_send(data)

    def get_config(self):
        """Return the current configuration as a string"""
        return f"frequency = {self.frequency} MHz, TX power = {self.tx_power} dBm, bandwidth = {self.bandwidth} kHz, spreading factor {self.spreading_factor}, coding rate = {self.coding_rate}"


def simulate_lora_send(data):
    """Simulate sending data via LoRa communication"""
    print(f"Sending data: {data}")
    time.sleep(0.5)
    print("Data sent successfully.")
    return True


def read_temperature():
    """Generate a random temperature reading"""
    return round(random.uniform(20.0, 25.0), 1)


def main():
    # Initialize and configure LoRa
    lora = LoRa()
    lora.set_mode(LoRa.MODE.STDBY)
    lora.set_frequency(868.1)
    lora.set_tx_power(14)
    lora.set_bandwidth(125)
    lora.set_spreading_factor(7)
    lora.set_coding_rate(5)

    print(f"Configured parameters: {lora.get_config()}")

    try:
        while True:
            temperature = read_temperature()
            lora.send(str(temperature))
            print("Pause for 10 seconds...")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
