# !/usr/bin/env python
# --------------------------------------------------------------------------- #
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# import logging
# FORMAT = ('%(asctime)-15s %(threadName)-15s '
#           '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

UNIT = 0x1


# def run_sync_client():
#     client = ModbusClient('localhost', port=5020)
#     client.connect()
#     log.debug("Write to a holding register and read back")
#     rq = client.write_register(0, 38, unit=UNIT)
#     rr = client.read_holding_registers(0, 1, unit=UNIT)
#     print(rr.registers[0])
#     client.close()


class valve_modbus_client:
    def __init__ (self, srv_port, srv_addres):
        self.valve_client = ModbusClient(srv_addres, port=srv_port)
    
    def valve_connect(self):
        self.valve_client.connect()
    
    def valve_disconnect(self):
        self.valve_client.close()

    def send_valve_server(self, valve_addres, valve_value):
        self.valve_client.write_register(valve_addres, valve_value, unit=UNIT)

    def get_value_server(self, valve_addres):
        self.valve_value = self.valve_client.read_holding_registers(valve_addres, 1, unit=UNIT)
        return self.valve_value.registers[0]


if __name__ == "__main__":
    valve_li = valve_modbus_client(5020, 'localhost')
    valve_li.valve_connect()
    valve_li.send_valve_server(0, 15)
    val = valve_li.get_value_server(0)
    print(val)

    # run_sync_client()
    