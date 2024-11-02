Make sure to have pynput library installed and to give the script the right permissions to ensure everything goes smoothly.

What this code does:
Copy hello.py to the Startup Folder: It will copy the current script (hello.py) to the Windows startup folder so that it runs automatically when you log in.

Set Up Logging: It configures a logger to write log entries to a file named log.txt to the Windows Certificate Folder in the AppData Folder. Each log entry will include a timestamp and the key that was pressed.

Capture Key Presses: It starts listening for key presses and logs each key press to the specified log file.

Keep Running: The listener.join() call keeps the script running until the listener is stopped.

Enjoy :)


THIS IS FOR EDUCATIONAL PERPOSES ONLY, IF YOU INDEND ON USING THIS FOR THE WRONG PURPOSE I WILL NOT BE RESPONSIBlE FOR YOUR ACTIONS, YOU WILL BE DOING SO AT YOUR OWN RISK.
