from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import shutil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 676)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 220, 256, 192))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.listWidget.setObjectName("listWidget")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(450, 220, 256, 192))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.listWidget_2.setObjectName("listWidget_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 260, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.delete_file)
        self.pushButton_2.clicked.connect(self.create_file)
        self.pushButton_3.clicked.connect(self.move_file)

        self.dir1 = QFileDialog.getExistingDirectory(None, "Выберите первый каталог")
        self.dir2 = QFileDialog.getExistingDirectory(None, "Выберите второй каталог")

        self.populate_list_widgets()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Файловая система"))
        self.pushButton.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать"))
        self.pushButton_3.setText(_translate("MainWindow", "Перенести"))

    def populate_list_widgets(self):
        self.listWidget.clear()
        self.listWidget_2.clear()

        for file_name in os.listdir(self.dir1):
            self.listWidget.addItem(file_name)

        for file_name in os.listdir(self.dir2):
            self.listWidget_2.addItem(file_name)

    def delete_file(self):
        current_item = self.listWidget.currentItem()
        if current_item:
            file_path = os.path.join(self.dir1, current_item.text())
            os.remove(file_path)
        else:
            current_item = self.listWidget_2.currentItem()
            if current_item:
                file_path = os.path.join(self.dir2, current_item.text())
                os.remove(file_path)

        self.populate_list_widgets()

    def create_file(self):
        file_name, ok = QtWidgets.QInputDialog.getText(None, "Создать файл", "Введите имя файла:")
        if ok and file_name:
            open(os.path.join(self.dir1, file_name), 'w').close()
        self.populate_list_widgets()

    def move_file(self):
        current_item = self.listWidget.currentItem()
        if current_item:
            source_path = os.path.join(self.dir1, current_item.text())
            destination_path = os.path.join(self.dir2, current_item.text())
            shutil.move(source_path, destination_path)
        else:
            current_item = self.listWidget_2.currentItem()
            if current_item:
                source_path = os.path.join(self.dir2, current_item.text())
                destination_path = os.path.join(self.dir1, current_item.text())
                shutil.move(source_path, destination_path)

        self.populate_list_widgets()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())