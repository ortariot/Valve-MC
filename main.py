import sys
from PyQt5 import QtWidgets

import valve_design
import valveModbusClient


class WindowsForms(QtWidgets.QMainWindow, valve_design.Ui_MainWindow, valveModbusClient.valve_modbus_client):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
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

    def slider_vlv2(self):
        value_vlv2 = self.vlv2_verticalSlider.value()
        self.vlv2_lcdNumber.display(value_vlv2)

    def slider_vlv3(self):
        value_vlv3 = self.vlv3_verticalSlider.value()
        self.vlv3_lcdNumber.display(value_vlv3)

    def slider_vlv4(self):
        value_vlv4 = self.vlv4_verticalSlider.value()
        self.vlv4_lcdNumber.display(value_vlv4)

    def btn_vlv1(self):
        print("button 1")

    def btn_vlv2(self):
        print("button 2")

    def btn_vlv3(self):
        print("button 3")

    def btn_vlv4(self):
        print("button 4")
    
    def opbtn(self):
        if self.opbtn_pushButton.text() == "Open":
            # valve_ip = self.ip_lineEdit.text()
            # valve_ip = 'localhost'
            # port = 5020
            # print(valve_ip)
            self.vlv_client = self.valve_modbus_client(5020, 'localhost')
            self.vlv_client.valve_connect()            
            self.opbtn_pushButton.setText("Close")
        elif self.opbtn_pushButton.text() == "Close":
            # self.vlv_client.valve_disconnect()
            self.opbtn_pushButton.setText("Open")
        # self.ip_lineEdit.displayText("suka")
        # print(valve_ip)






def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = WindowsForms()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
