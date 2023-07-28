from  PyQt5.QtWidgets import *
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import os
import tempfile

status=None
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 778)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(42, 42, 65);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setStyleSheet("background-color: rgb(27, 27, 42);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 15777216))
        self.stackedWidget.setStyleSheet("background-color: rgb(27, 27, 42);\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_22 = QtWidgets.QFrame(self.page_6)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_22.setStyleSheet("background-color: rgb(27, 27, 42);\n"
"border-radius:10px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_58 = QtWidgets.QFrame(self.frame_22)
        self.frame_58.setMinimumSize(QtCore.QSize(400, 110))
        self.frame_58.setMaximumSize(QtCore.QSize(99999, 200))
        self.frame_58.setStyleSheet("background-color: rgb(16, 16, 26);\n"
"border-radius:6px;")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_38 = QtWidgets.QLabel(self.frame_58)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_6.addWidget(self.label_38, 0, QtCore.Qt.AlignLeft)
        self.frame_50 = QtWidgets.QFrame(self.frame_58)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_50)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(518, 40))
        self.lineEdit_12.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(33, 33, 50);\n"
"    border-radius: 9px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_3.addWidget(self.lineEdit_12)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_50)
        self.pushButton_17.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_17.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(33, 33, 50);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        self.verticalLayout_6.addWidget(self.frame_50)
        self.verticalLayout.addWidget(self.frame_58)
        self.frame_60 = QtWidgets.QFrame(self.frame_22)
        self.frame_60.setMinimumSize(QtCore.QSize(400, 150))
        self.frame_60.setMaximumSize(QtCore.QSize(9999, 200))
        self.frame_60.setStyleSheet("background-color: rgb(16, 16, 26);\n"
"border-radius:6px;")
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_60)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_41 = QtWidgets.QLabel(self.frame_60)
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_10.addWidget(self.label_41)
        self.frame_2 = QtWidgets.QFrame(self.frame_60)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_45 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_12.addWidget(self.label_45)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_16.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(33, 33, 50);\n"
"    border-radius: 9px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_12.addWidget(self.lineEdit_16)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_43 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_43.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_8.addWidget(self.label_43)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_14.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(33, 33, 50);\n"
"    border-radius: 9px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_8.addWidget(self.lineEdit_14)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_44 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_9.addWidget(self.label_44)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_15.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(33, 33, 50);\n"
"    border-radius: 9px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 9px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_9.addWidget(self.lineEdit_15)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_10.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_60)
        self.frame_27 = QtWidgets.QFrame(self.frame_22)
        self.frame_27.setStyleSheet("background-color: rgb(16, 16, 26);\n"
"border-radius:6px;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_27)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setStyleSheet("background-color: rgb(16, 16, 26);\n"
"border-radius:6px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 85, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_14.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(33, 33, 50);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_27)
        self.verticalLayout_3.addWidget(self.frame_22)
        self.stackedWidget.addWidget(self.page_6)
        self.verticalLayout_11.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Classdojo</span><span style=\" font-size:16pt;\"> Data Downloader</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "Select Output folder"))
        self.pushButton_17.setText(_translate("MainWindow", "Browse"))
        self.label_41.setText(_translate("MainWindow", "Settings"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p>Your dojo log session id</p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "Your dojo login.sid"))
        self.label_44.setText(_translate("MainWindow", "Your dojo home login.sid"))
        self.label.setText(_translate("MainWindow", "1 Downloaded"))
        self.pushButton_14.setText(_translate("MainWindow", "Start"))

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('')
        self.ui.setupUi(self)

        self.FEED_URL = 'https://home.classdojo.com/api/storyFeed?includePrivate=true'
        self.DESTINATION = ""
        self.SESSION_COOKIES = {
            'dojo_log_session_id': self.ui.lineEdit_16.text(),
            'dojo_login.sid': self.ui.lineEdit_14.text(),
            'dojo_home_login.sid': self.ui.lineEdit_15.text(),
        }
        self.ui.lineEdit_16.setText("f1b8f575-2a00-435b-a694-f2812ebec778")
        self.ui.lineEdit_14.setText("s%3A5NOyFXb9NMTlI3_alOQbVzGtH3AQ2xBO.mxgqKh%2FFdk%2B4bFszbSc6EE8n54ysjHwLybKJjjdEOx8")
        self.ui.lineEdit_15.setText("s:5NOyFXb9NMTlI3_alOQbVzGtH3AQ2xBO.mxgqKh/Fdk+4bFszbSc6EE8n54ysjHwLybKJjjdEOx8")

        self.NOT_BEFORE = '0000-00-00'  # '2020-08-22'


        self.ui.pushButton_17.clicked.connect(self.select_folder)
        self.ui.pushButton_14.clicked.connect(self.start_program)



    def main(self):
        print('Starting')
        self.ui.label.setText("Starting")
        contents, total = self.get_contents(self.FEED_URL)
        self.download_contents(contents, total)
    # threading
    def stop_process(self):
        global status
        status=None
        pass

    def start_program(self):
        global status
        self.DESTINATION = tempfile.mkdtemp(
            dir=self.ui.lineEdit_12.text())  # make sure this directory exists in the same place as this script.
        self.SESSION_COOKIES = {
            'dojo_log_session_id': self.ui.lineEdit_16.text(),
            'dojo_login.sid': self.ui.lineEdit_14.text(),
            'dojo_home_login.sid': self.ui.lineEdit_15.text(),
        }

        print(self.SESSION_COOKIES)
        s=threading.Thread(target=self.main)
        s.start()
        status=True
        self.ui.pushButton_14.setDisabled(True)

    def get_items(self,feed_url):

        print('Fetching items: %s ...' % feed_url)
        resp = requests.get(feed_url, cookies=self.SESSION_COOKIES)
        data = resp.json()
        prev = data.get('_links', {}).get('prev', {}).get('href')

        return data['_items'], prev

    def select_folder(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Output Folder"))
        self.ui.lineEdit_12.setText(file)
    def get_contents(self,feed_url):
        items, prev = self.get_items(feed_url)
        count = 0
        while prev and feed_url != prev:
            prev_urls, prev = self.get_items(prev)
            items.extend(prev_urls)
            count += 1


        # Save the JSON data for later/inspection.
        with open(os.path.join(self.DESTINATION, 'data.json'), 'w') as fd:
            fd.write(json.dumps(items, indent=4))

        contents = []
        total = 0
        for item in items:
            data = item['contents']
            entry = {
                'description': data.get('body'),
                'base_name': None,
                'day': None,
                'attachments': [],
            }
            attachments = data.get('attachments', {})
            if not attachments:
                continue

            for attachment in attachments:
                parts = attachment['path'].split('/')
                day = parts[-3]
                if parts[3] == 'api' or day < self.NOT_BEFORE:
                    continue
                total += 1
                if not entry['base_name']:
                    entry['base_name'] = parts[-4]
                    entry['day'] = day
                entry['attachments'].append({'name': '_'.join(parts[-2:]),
                                             'url': attachment['path']})

            if entry['base_name']:
                contents.append(entry)

        return contents, total

    def download_contents(self,contents, total):
        index = 0
        highest_day = contents[0]['day']
        for entry in contents:
            description_name = '{}_{}_description.txt'.format(entry['day'],
                                                              entry['base_name'])
            with open(os.path.join(self.DESTINATION, description_name), 'wt') as fd:
                fd.write(entry['description'])
            for item in entry['attachments']:
                index += 1
                day = entry['day']
                if day > highest_day:
                    highest_day = day
                url = item['url']
                filename = os.path.join(self.DESTINATION,
                                        '{}_{}_{}'.format(entry['day'],
                                                          entry['base_name'],
                                                          item['name']))
                if os.path.exists(filename):
                    continue
                print('Downloading {}/{} on {}: {}'
                      .format(index, total, day, item['name']))
                self.ui.label.setText('Downloading {}/{} on {}: {}'
                      .format(index, total, day, item['name']))
                with open(filename, 'wb') as fd:
                    resp = requests.get(url, cookies=self.SESSION_COOKIES)
                    fd.write(resp.content)
        print('Last day of data download: {}'.format(highest_day))
        self.ui.label.setText('Last day of data download: {}'.format(highest_day))
        print('Done!')
        self.ui.label.setText('Done!')
        self.ui.pushButton_14.setDisabled(False)


from sys import exit as sysExit

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())