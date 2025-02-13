# USB Keylogger with Automation Potential  

## Overview  

This project consists of two parts:  

- **cncserver.py:** A simple command and control (C&C) server that accepts incoming TCP connections, logs connection details of incoming clients, and displays incoming data.  
- **system_process.py:** A system process logger that records key presses and mouse events using the `pynput` library. The events are logged to files on a specified USB drive and also sent in real-time to the C&C server.  

## Table of Contents  

- [Overview](#overview)  
- [Components](#components)  
- [cncserver.py](#cncserverpy)  
- [system_process.py](#system_processpy)  
- [Configuration](#configuration)  
- [Automation Potential](#automation-potential)  
- [Running the Project](#running-the-project)  
- [Public IP & Port Forwarding](#public-ip--port-forwarding)  

## Components  

### cncserver.py  

- **What It Does:**  
  Sets up a server that listens on `localhost:12345` (by default), accepts incoming connections, and echoes whatever data it receives.  
- **How to Run:**  
  ```bash  
  python3 cncserver.py  
  ```  

### system_process.py  

- **What It Does:**  
  - Monitors keyboard and mouse events using `pynput`.  
  - Logs the events to a USB drive (default location: `E:`) in `log_data.txt` (detailed logs) and `system_info.txt` (summary logs).  
  - Sends logs to the C&C server over TCP.  

- **How to Run:**  
  ```bash  
  python3 system_process.py  
  ```  
  _Note: Make sure your USB drive is mounted at the specified path, or update the script accordingly._  

## Configuration  

- **IP Address and Port Configuration:**  
  - Both scripts default to `localhost` on port `12345`.  
  - To run over a public IP, update:  
    - `SERVER_HOST` in `cncserver.py`  
    - `SERVER_IP` in `system_process.py`  
  - Configure port forwarding on your router to direct incoming traffic to the server machine via your public IP.  

- **Dependencies:**  
  - Python 3  
  - `pynput` (install with `pip install pynput`)  

## Automation Potential  

This setup isn't just for occasional use—it's ideal for automation:  

- **Scheduled Execution:**  
  Use cron (Linux/macOS) or Task Scheduler (Windows) to automatically run `system_process.py` at system startup or at regular intervals.  

- **Remote Management:**  
  With proper configuration and port forwarding, you can expand the system to monitor multiple machines or automate the collection of system metrics remotely.  

- **Integration:**  
  This project can be integrated with other automation tools or scripts to create a more advanced remote logging and monitoring system. Its simple design allows it to be easily incorporated into larger workflows.  

## Running the Project  

1. **Start the Server:**  
   On your server machine, run:  
   ```bash  
   python3 cncserver.py  
   ```  

2. **Launch the Logger:**  
   On the client machine(s), run:  
   ```bash  
   python3 system_process.py  
   ```  

The logger records keyboard and mouse events and sends them to the server, which logs and displays the incoming data.  

## Public IP & Port Forwarding  

If you need to run this system over the internet:  
- **Set Up Port Forwarding:**  
  Forward a selected port on your router to the machine running `cncserver.py`.  
- **Update Configuration:**  
  Replace `localhost` in both scripts with your public IP or a dynamic DNS address.  

---
