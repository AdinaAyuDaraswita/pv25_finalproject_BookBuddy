import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from loginUi import Ui_Form
from bookBuddyFix import Ui_MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Event tombol login
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "Adina" and password == "F1D022030":
            self.main_window = QMainWindow()
            self.ui_main = Ui_MainWindow()
            self.ui_main.setupUi(self.main_window)

            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
