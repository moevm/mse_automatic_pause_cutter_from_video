from PyQt5.QtWidgets import QMessageBox

class MessageBox:
    def __init__(self, type, message):
        if(type == 'error' or type == 'info') :
            self.message_box = QMessageBox()
            self.message_box.setInformativeText(message)
            if(type == 'error') :
                self.message_box.setIcon(QMessageBox.Critical)
                self.message_box.setText("Ошибка")
                self.message_box.setWindowTitle("Ошибка")
            elif(type == 'info') :
                self.message_box.setIcon(QMessageBox.Information)
                self.message_box.setText("Информация")
                self.message_box.setWindowTitle("Информация")
        else:
            raise Exception("Неизвестный тип сообщения")

    def show(self):
        self.message_box.show()
        self.message_box.exec()

    def hide(self):
        self.message_box.accept()