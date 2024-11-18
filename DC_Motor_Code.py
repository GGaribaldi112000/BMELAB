import serial
import time

# Replace 'COM3' with the correct port for your Arduino
# On Linux/Mac, it could be '/dev/ttyUSB0' or '/dev/ttyACM0'
arduino_port = 'COM4'
baud_rate = 9600

try:
    # Establish serial connection
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for the connection to initialize

    def motor_control(command):
        if command in ['F', 'B', 'S']:
            arduino.write(command.encode())
            print(f"Sent command: {command}")
        else:
            print("Invalid command! Use 'F' for Forward, 'B' for Backward, 'S' for Stop.")

    while True:
        user_input = input("Enter command (F: Forward, B: Backward, S: Stop, Q: Quit): ").upper()
        if user_input == 'Q':
            print("Exiting program.")
            break
        motor_control(user_input)

except serial.SerialException as e:
    print(f"Error: {e}")
finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
