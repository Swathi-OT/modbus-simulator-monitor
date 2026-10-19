from pymodbus.client import ModbusTcpClient
from datetime import datetime
import time

client = ModbusTcpClient("localhost", port=502)
client.connect()

print("Modbus Monitor — Reading PLC Registers")
print("-" * 40)

try:
    while True:
        # Must use keyword arguments in newer pymodbus
        result = client.read_holding_registers(address=0, count=3)
        
        if not result.isError():
            timestamp = datetime.now().strftime("%H:%M:%S")
            temp = result.registers[0]
            humidity = result.registers[1]
            pressure = result.registers[2]
            print(f"[{timestamp}] Temp:{temp}°C | Humidity:{humidity}% | Pressure:{pressure}hPa")
        else:
            print("Error reading registers:", result)
        time.sleep(2)
except KeyboardInterrupt:
    print("\nMonitor stopped")
    client.close()
