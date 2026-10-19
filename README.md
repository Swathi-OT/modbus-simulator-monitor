# Modbus Protocol Simulator + Monitor

A beginner-friendly Operational Technology (OT) cybersecurity project that simulates a Programmable Logic Controller (PLC) and monitors Modbus TCP communication using Python.

This project demonstrates how industrial devices exchange data through the Modbus TCP protocol. It provides a simple laboratory environment for learning industrial communication, register monitoring, and the fundamentals of OT security.

## Project Objectives

- Understand the Modbus TCP client-server communication model.
- Simulate a PLC using a Modbus TCP server.
- Monitor industrial process values using a Modbus client.
- Read and write Modbus holding registers.
- Build a foundation for industrial network monitoring and OT intrusion detection.

## Features

- Simulated PLC using a Modbus TCP server.
- Modbus TCP client for monitoring register values.
- Holding-register monitoring for temperature, humidity, and pressure.
- Support for updating register values.
- Periodic display of process values.
- Simple Python implementation suitable for beginners.

## Project Structure

```text
modbus-simulator-monitor/
├── plc_server.py
├── modbus_monitor.py
├── README.md
└── .gitignore
```

### File Description

- `plc_server.py` — runs the simulated PLC and provides Modbus TCP register access.
- `modbus_monitor.py` — connects to the server and reads process values.
- `README.md` — documents the project and usage instructions.
- `.gitignore` — excludes temporary files and local environment folders from Git.

## Technologies Used

- Python 3
- Modbus TCP
- PyModbus
- Kali Linux or another Linux distribution
- Git and GitHub

## Requirements

- Python 3 installed.
- `pip` for installing Python packages.
- The project Python scripts.
- A local machine or isolated lab environment for testing.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Swathi-OT/modbus-simulator-monitor.git
cd modbus-simulator-monitor
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install PyModbus

```bash
python -m pip install pymodbus
```

**Compatibility note:** PyModbus APIs can differ between versions. Use the version compatible with the imports and server/client methods in the project's Python scripts.

## How to Run

### Step 1: Start the Simulated PLC

Open Terminal 1, activate the virtual environment if needed, and run:

```bash
python plc_server.py
```

The server should start listening for Modbus TCP connections. If your script prints a startup message, it may show the configured port and initial register values.

### Step 2: Start the Modbus Monitor

Open Terminal 2 in the same project folder. Activate the virtual environment and run:

```bash
python modbus_monitor.py
```

The monitor should connect to the local server and periodically display the process values read from the holding registers.

Example output, depending on the implementation:

```text
[09:35:12] Temp: 25°C | Humidity: 60% | Pressure: 1013 hPa
[09:35:14] Temp: 25°C | Humidity: 60% | Pressure: 1013 hPa
```

The displayed output depends on the register mapping and formatting implemented in the scripts.

## Updating Register Values

If the server supports register writes, a Modbus client can update values for testing.

For example, the following client code illustrates the concept. Confirm the register addresses and PyModbus API against your server implementation before running it.

```python
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)

try:
    if client.connect():
        response = client.write_register(address=0, value=32)
        print("Write response:", response)

        response = client.write_register(address=1, value=75)
        print("Write response:", response)
    else:
        print("Could not connect to the Modbus server.")
finally:
    client.close()
```

Use this only against your own local simulator or another system you are authorized to test. The monitor should display the updated values if the register mapping is correct.

## Understanding Modbus TCP

Modbus TCP is an industrial communication protocol used to exchange data between devices such as PLCs, HMIs, and monitoring applications.

In this project:

1. The simulated PLC acts as the Modbus TCP server.
2. The monitor acts as the Modbus TCP client.
3. The server exposes process values through holding registers.
4. The client reads register values and displays them.
5. Authorized test writes can change register values if the server permits them.

Modbus TCP commonly uses TCP port `502`. The actual port used by this project depends on the server configuration.

## OT Cybersecurity Relevance

Industrial communication monitoring is an important part of OT cybersecurity. Understanding normal Modbus traffic provides a starting point for identifying unexpected behavior.

Potential future security checks include:

- Unexpected register write operations.
- Repeated or unusually frequent requests.
- Communication from unknown clients.
- Access to sensitive registers.
- Unusual function-code usage.

**Current scope:** This project is a learning simulator and monitor. It should not be described as a production-ready intrusion detection system unless those security checks have been implemented and tested.

## Future Improvements

- Add logging with timestamps.
- Detect unexpected register writes.
- Monitor request frequency and unusual communication patterns.
- Add configurable alerts.
- Capture and analyze Modbus TCP packets using Wireshark or Scapy.
- Add a simple dashboard for displaying process values.
- Integrate rule-based detection into a broader industrial intrusion detection system.

## Learning Outcomes

By completing this project, learners can gain practical experience with:

- Modbus TCP client-server communication.
- PLC simulation concepts.
- Industrial register reading and writing.
- Python networking libraries.
- The fundamentals of OT network monitoring.
- The relationship between industrial protocols and cybersecurity.

## Safety Note

This project is intended for educational use in a local, isolated lab. Do not test register writes or security experiments against production PLCs or industrial systems without explicit authorization.

## Author

**Swathi S**

OT / IoT Cybersecurity Learner

## Disclaimer

This is an educational project developed for learning and portfolio purposes. It is not a substitute for a validated industrial monitoring or security solution.
