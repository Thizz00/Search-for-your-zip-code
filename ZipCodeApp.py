from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import sys
from static.Pushbuttonstyle import Stylesheetpushbutton
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        Form.setFont(font)

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 30, 381, 491))
        self.frame.setStyleSheet("border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 381, 491))
        self.frame_2.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n""border-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 341, 461))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0,0,0,100);\n""border-radius:20px\n""")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;\n")
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 200, 211, 21))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n""border:none;\n""border-bottom:2px solid rgba(255,255,255,255);\n""color:rgba(255,255,255,230);\n""padding-bottom:7px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 290, 211, 21))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n""border:none;\n""border-bottom:2px solid rgba(255,255,255,255);\n""color:rgba(255,255,255,230);\n""padding-bottom:7px;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 350, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n""{\n""background-color:#9E9E0A;\n""border-radius:10px;\n""color:white;\n""}\n""QPushButton:hover\n""{\n""background-color:#F9F956;\n""\n""}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.load_city_data())

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(110, 390, 248, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:rgba(0,0,0,0);\n""border:none;\n""color:white \n""text-align:center")
        self.textBrowser.setObjectName("textBrowser")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 490, 261, 31))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")

        self.pushButton_closeapp = QtWidgets.QPushButton(Form)
        self.pushButton_closeapp.setGeometry(QtCore.QRect(380, 30, 55, 45))
        font = QtGui.QFont()
        font.setFamily("font bottons music")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_closeapp.setFont(font)
        self.pushButton_closeapp.setStyleSheet(Stylesheetpushbutton.Pushbuttonstyles(self))
        self.pushButton_closeapp.setObjectName("pushButton_2")
        self.pushButton_closeapp.clicked.connect(lambda:sys.exit())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Find your Zip Code"))
        self.lineEdit.setPlaceholderText(_translate("Form", "City e.g. Kraków"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Country e.g. PL"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_3.setText(_translate("Form", "All right reserved. Jakub Kiełb 2021 © "))
        self.pushButton_closeapp.setText(_translate("Form", "t"))

    def load_city_data(self):
            if len(self.lineEdit.text())==0 or len(self.lineEdit_2.text())==0:
                self.lineEdit.setPlaceholderText("City e.g. Kraków")
                self.lineEdit_2.setPlaceholderText("Country e.g. PL")
            else:
                try:
                    headers = { 
                    "apikey": "Your-Api-key-from-zipcodebase.com"}
                    params = (
                    ("city",self.lineEdit.text()),
                    ("country",self.lineEdit_2.text()),
                    );
                    response = requests.get('https://app.zipcodebase.com/api/v1/code/city', headers=headers, params=params);
                    for i in response.json()['results']:
                        self.textBrowser.append(i)
                except:
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit.setPlaceholderText("City e.g. Kraków")
                    self.lineEdit_2.setPlaceholderText("Country e.g. PL")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
