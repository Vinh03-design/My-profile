from PyQt5 import QtCore, QtGui, QtWidgets

# lib hide taskbar
from PyQt5.QtCore import Qt

class Ui_ExitDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

       # Set the window flags to hide taskbar icon and remove window borders
        Dialog.setWindowFlags(Qt.Tool)  # Hide the taskbar icon
        Dialog.setWindowFlag(Qt.FramelessWindowHint)  # Optional: remove window borders

        Dialog.resize(350, 200)
        Dialog.setMaximumSize(QtCore.QSize(350, 200))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("alternate-background-color: rgb(14, 255, 122);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(350, 200))
        self.frame.setMaximumSize(QtCore.QSize(350, 200))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(350, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(350, 40))
        self.label.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(350, 35))
        self.label_2.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(350, 40))
        self.label_3.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(350, 65))
        self.frame_5.setMaximumSize(QtCore.QSize(350, 65))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 30px;\n"
"border-bottom-right-radius: 30px;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setMinimumSize(QtCore.QSize(175, 65))
        self.pushButton_2.setMaximumSize(QtCore.QSize(175, 65))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border-bottom-left-radius: 30px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top: 1px solid rgba(160, 160, 160,90);\n"
"border-right: 1px solid rgba(160, 160, 160,90);")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons_for_exit/Icons_exit/Yes.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setMinimumSize(QtCore.QSize(175, 65))
        self.pushButton.setMaximumSize(QtCore.QSize(175, 65))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border-bottom-right-radius: 30px;\n"
"border-bottom-left-radius: 0px;\n"
"border-top: 1px solid rgba(160, 160, 160,90);\n"
"border-right: 1px solid rgba(160, 160, 160,90);")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons_for_exit/Icons_exit/No.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.pushButton_2.clicked.connect(self.exit_yes)

        self.pushButton.clicked.connect(lambda: self.exit_no(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def exit_no(self, Dialog):
        """Closes the dialog when the button is clicked."""
        Dialog.close()  # Close the dialog

    def exit_yes(self):
            exit()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Confirmation</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Are you sure you want to exit </p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">this app</p></body></html>"))
import Icons_exit



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ExitDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
