import sys
from PyQt5 import QtWidgets, QtGui

class LoginForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.usernameLabel = QtWidgets.QLabel("Username:", self)
        self.usernameLineEdit = QtWidgets.QLineEdit(self)

        self.passwordLabel = QtWidgets.QLabel("Password:", self)
        self.passwordLineEdit = QtWidgets.QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.securityCodeLabel = QtWidgets.QLabel("Security Code:", self)
        self.securityCodeLineEdit = QtWidgets.QLineEdit(self)

        self.loginButton = QtWidgets.QPushButton("Login", self)
        self.loginButton.clicked.connect(self.handleLogin)

        layout = QtWidgets.QFormLayout(self)
        layout.addRow(self.usernameLabel, self.usernameLineEdit)
        layout.addRow(self.passwordLabel, self.passwordLineEdit)
        layout.addRow(self.securityCodeLabel, self.securityCodeLineEdit)
        layout.addRow(self.loginButton)

    def handleLogin(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        securityCode = self.securityCodeLineEdit.text()

        
        if username == "admin" and password == "password" and securityCode == "1234":
            
            QtWidgets.QMessageBox.information(self, "Login", "Login successful!")
        else:
        
            QtWidgets.QMessageBox.warning(self, "Login", "Login failed. Try again.")

app = QtWidgets.QApplication(sys.argv)
form = LoginForm()
form.show()
sys.exit(app.exec_())
