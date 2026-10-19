from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock

# Start at address 1 (required in newer pymodbus)
store = ModbusDeviceContext(
    di=ModbusSequentialDataBlock(1, [0]*100),
    co=ModbusSequentialDataBlock(1, [0]*100),
    hr=ModbusSequentialDataBlock(1, [25, 60, 1013] + [0]*97),  # Temp, Humidity, Pressure
    ir=ModbusSequentialDataBlock(1, [0]*100)
)

context = ModbusServerContext(devices=store, single=True)

print("Simulated PLC running on port 502")
print("Registers: Temperature=25, Humidity=60, Pressure=1013")
print("Press Ctrl+C to stop")
StartTcpServer(context=context, address=("localhost", 502))
