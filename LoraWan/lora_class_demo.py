from lora_module import LoRa
import random
import time


def main():
    # Initialize LoRa Module
    lora = LoRa()
    lora.set_mode(LoRa.MODE.STDBY)  # Fixed typo: Lora → LoRa

    lora.set_frequency(868.1)
    lora.set_tx_power(14)
    lora.set_bandwidth(125)
    lora.set_spreading_factor(7)
    lora.set_coding_rate(5)

    print("LoRa module initialized.")
    print(f"Configured parameters: {lora.get_config()}")  # Use the get_config method

    try:
        while True:
            # Generate random temperature
            temperature = round(random.uniform(20.0, 25.0), 1)
            print(f"Temperature reading: {temperature}")
            lora.send(str(temperature))  # Send data
            print("Pausing for 10 seconds...\n")
            # Wait 60 seconds before sending again
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
