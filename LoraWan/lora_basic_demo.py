import random
import time


def simulate_lora_send(data):
    print(f"Sending data: {data}")
    time.sleep(1)
    print("Data sent successfully.")
    return True


def read_temperature():
    return round(random.uniform(20.0, 25.0), 1)


def main():
    try:
        while True:
            temperature = read_temperature()  # Get random temperature
            simulate_lora_send(temperature)  # Simulate sending data
            print("Pausing for 10 seconds...\n")
            time.sleep(10)  # Wait 60 seconds before sending again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
