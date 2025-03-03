import os

def initialize_display(num_sensors):
    """Prints the initial console layout."""
    print("Current temperatures:\n")
    for i in range(num_sensors):
        print(f"Latest Temperatures: Sensor {i}: --°C")
    for i in range(num_sensors):
        print(f"Sensor {i} Average: {' ' * 50} --°C")

def update_display(num_sensors, latest_temperatures, temperature_averages):
    """Refreshes the console display with real-time sensor data."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Current temperatures:\n")

    for i in range(num_sensors):
        temp = latest_temperatures.get(i, "--")
        print(f"Latest Temperatures: Sensor {i}: {temp}°C")

    for i in range(num_sensors):
        avg = temperature_averages.get(i, "--")
        print(f"Sensor {i} Average: {' ' * 50} {avg:.2f}°C")
