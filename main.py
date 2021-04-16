import sys
from PyQt5 import QtWidgets

import valve_design
import valveModbusClient


class WindowsForms(QtWidgets.QMainWindow, valve_design.Ui_MainWindow, valveModbusClient.valve_modbus_client):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.vlv1_verticalSlider.setRange(0, 100)
        self.vlv1_verticalSlider.valueChanged.connect(self.slider_vlv1)
        self.vlv2_verticalSlider.setRange(0, 100)
        self.vlv2_verticalSlider.valueChanged.connect(self.slider_vlv2)
        self.vlv3_verticalSlider.setRange(0, 100)
        self.vlv3_verticalSlider.valueChanged.connect(self.slider_vlv3)
        self.vlv4_verticalSlider.setRange(0, 100)
        self.vlv4_verticalSlider.valueChanged.connect(self.slider_vlv4)
        self.vlv1_button.clicked.connect(self.btn_vlv1)
        self.vlv2_button.clicked.connect(self.btn_vlv2)
        self.vlv3_button.clicked.connect(self.btn_vlv3)
        self.vlv4_button.clicked.connect(self.btn_vlv4)
        self.opbtn_pushButton.clicked.connect(self.opbtn)

    def slider_vlv1(self):
        value_vlv1 = self.vlv1_verticalSlider.value()
        self.vlv1_lcdNumber.display(value_vlv1)
        self.vlv_client.send_value_valve_server(0, value_vlv1)

    def slider_vlv2(self):
        value_vlv2 = self.vlv2_verticalSlider.value()
        self.vlv2_lcdNumber.display(value_vlv2)
        self.vlv_client.send_value_valve_server(1, value_vlv2)

    def slider_vlv3(self):
        value_vlv3 = self.vlv3_verticalSlider.value()
        self.vlv3_lcdNumber.display(value_vlv3)
        self.vlv_client.send_value_valve_server(2, value_vlv3)

    def slider_vlv4(self):
        value_vlv4 = self.vlv4_verticalSlider.value()
        self.vlv4_lcdNumber.display(value_vlv4)
        self.vlv_client.send_value_valve_server(3, value_vlv4)

    def btn_vlv1(self):
        if self.vlv1_button.text() == "VALVE1 ON":
            self.vlv_client.send_coil_valve_server(0, True)
            self.vlv1_button.setText("VALVE1 OFF")
            self.vlv1_verticalSlider.setEnabled(True)
        elif self.vlv1_button.text() == "VALVE1 OFF":
            self.vlv_client.send_coil_valve_server(0, False)
            self.vlv1_button.setText("VALVE1 ON")
            self.vlv1_verticalSlider.setEnabled(False)

    def btn_vlv2(self):
        if self.vlv2_button.text() == "VALVE2 ON":
            self.vlv_client.send_coil_valve_server(1, True)
            self.vlv2_button.setText("VALVE2 OFF")
            self.vlv2_verticalSlider.setEnabled(True)
        elif self.vlv2_button.text() == "VALVE2 OFF":
            self.vlv_client.send_coil_valve_server(1, False)
            self.vlv2_button.setText("VALVE2 ON")
            self.vlv2_verticalSlider.setEnabled(False)

    def btn_vlv3(self):
        if self.vlv3_button.text() == "VALVE3 ON":
            self.vlv_client.send_coil_valve_server(2, True)
            self.vlv3_button.setText("VALVE3 OFF")
            self.vlv3_verticalSlider.setEnabled(True)
        elif self.vlv3_button.text() == "VALVE3 OFF":
            self.vlv_client.send_coil_valve_server(2, False)
            self.vlv3_button.setText("VALVE3 ON")
            self.vlv3_verticalSlider.setEnabled(False)

    def btn_vlv4(self):
        if self.vlv4_button.text() == "VALVE4 ON":
            self.vlv_client.send_coil_valve_server(3, True)
            self.vlv4_button.setText("VALVE4 OFF")
            self.vlv4_verticalSlider.setEnabled(True)
        elif self.vlv4_button.text() == "VALVE4 OFF":
            self.vlv_client.send_coil_valve_server(3, False)
            self.vlv4_button.setText("VALVE4 ON")
            self.vlv4_verticalSlider.setEnabled(False)
    
    def opbtn(self):
        if self.opbtn_pushButton.text() == "Open":
            valve_ip = self.ip_lineEdit.text()
            port = 5020
            self.vlv_client = valveModbusClient.valve_modbus_client(port, valve_ip)
            self.vlv_client.valve_connect()     
            self.vlv1_frame.setEnabled(True) 
            self.vlv2_frame.setEnabled(True) 
            self.vlv3_frame.setEnabled(True) 
            self.vlv4_frame.setEnabled(True) 
            self.ip_lineEdit.setEnabled(False)
            self.opbtn_pushButton.setText("Close")
        elif self.opbtn_pushButton.text() == "Close":
            self.vlv_client.valve_disconnect()

            self.opbtn_pushButton.setText("Open")
            self.vlv1_frame.setEnabled(False)  
            self.vlv2_frame.setEnabled(False) 
            self.vlv3_frame.setEnabled(False)
            self.vlv4_frame.setEnabled(False) 
            self.ip_lineEdit.setEnabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = WindowsForms()  
    window.show()  
    app.exec_() 


if __name__ == '__main__':
    main()
