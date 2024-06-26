# Form implementation generated from reading ui file 'd:\Python_PORTFOLIO312\15_port_scanner\App_main\UI\ports_scan.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mw_main(object):
    def setupUi(self, mw_main):
        mw_main.setObjectName("mw_main")
        mw_main.resize(576, 595)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        mw_main.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=mw_main)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_scan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_scan.setGeometry(QtCore.QRect(310, 180, 111, 31))
        self.pb_scan.setObjectName("pb_scan")
        self.lb_target_port = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_target_port.setGeometry(QtCore.QRect(50, 50, 91, 31))
        self.lb_target_port.setObjectName("lb_target_port")
        self.le_target_port = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_target_port.setGeometry(QtCore.QRect(250, 50, 181, 31))
        self.le_target_port.setObjectName("le_target_port")
        self.le_ports_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_ports_amount.setGeometry(QtCore.QRect(250, 90, 181, 31))
        self.le_ports_amount.setObjectName("le_ports_amount")
        self.le_threads_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_threads_amount.setGeometry(QtCore.QRect(250, 129, 181, 31))
        self.le_threads_amount.setObjectName("le_threads_amount")
        self.lb_ports_amount = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_ports_amount.setGeometry(QtCore.QRect(50, 90, 181, 31))
        self.lb_ports_amount.setObjectName("lb_ports_amount")
        self.lb_threads_amount = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_threads_amount.setGeometry(QtCore.QRect(50, 130, 141, 31))
        self.lb_threads_amount.setObjectName("lb_threads_amount")
        self.pb_cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(450, 410, 111, 31))
        self.pb_cancel.setObjectName("pb_cancel")
        self.lb_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_message.setGeometry(QtCore.QRect(20, 460, 531, 91))
        self.lb_message.setObjectName("lb_message")
        self.lb_ports_to_del = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_ports_to_del.setGeometry(QtCore.QRect(50, 320, 141, 31))
        self.lb_ports_to_del.setObjectName("lb_ports_to_del")
        self.le_ports_to_del = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.le_ports_to_del.setGeometry(QtCore.QRect(50, 360, 501, 31))
        self.le_ports_to_del.setObjectName("le_ports_to_del")
        self.pb_close_selected = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_close_selected.setGeometry(QtCore.QRect(60, 410, 161, 31))
        self.pb_close_selected.setObjectName("pb_close_selected")
        self.pb_close_all = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_close_all.setGeometry(QtCore.QRect(260, 410, 151, 31))
        self.pb_close_all.setObjectName("pb_close_all")
        self.lb_le_found_ports = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_le_found_ports.setGeometry(QtCore.QRect(50, 280, 510, 31))
        self.lb_le_found_ports.setText("")
        self.lb_le_found_ports.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_le_found_ports.setObjectName("lb_le_found_ports")
        self.lb_found_ports = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_found_ports.setGeometry(QtCore.QRect(50, 240, 141, 31))
        self.lb_found_ports.setObjectName("lb_found_ports")
        self.pb_apply_to_scan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_apply_to_scan.setGeometry(QtCore.QRect(170, 180, 121, 31))
        self.pb_apply_to_scan.setObjectName("pb_apply_to_scan")
        self.pb_clean_entries = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pb_clean_entries.setGeometry(QtCore.QRect(440, 180, 121, 31))
        self.pb_clean_entries.setObjectName("pb_clean_entries")
        self.lb_or = QtWidgets.QLabel(parent=self.centralwidget)
        self.lb_or.setGeometry(QtCore.QRect(230, 410, 21, 31))
        self.lb_or.setObjectName("lb_or")
        mw_main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mw_main)
        self.statusbar.setObjectName("statusbar")
        mw_main.setStatusBar(self.statusbar)

        self.retranslateUi(mw_main)
        QtCore.QMetaObject.connectSlotsByName(mw_main)

    def retranslateUi(self, mw_main):
        _translate = QtCore.QCoreApplication.translate
        mw_main.setWindowTitle(_translate("mw_main", "Port Scanner"))
        self.pb_scan.setText(_translate("mw_main", "Scan Ports"))
        self.lb_target_port.setText(_translate("mw_main", "Target port:"))
        self.le_target_port.setPlaceholderText(_translate("mw_main", "eg: 127.0.0.1"))
        self.le_ports_amount.setPlaceholderText(_translate("mw_main", "eg: 600"))
        self.le_threads_amount.setPlaceholderText(_translate("mw_main", "eg:200"))
        self.lb_ports_amount.setText(_translate("mw_main", "Amount of ports to scan:"))
        self.lb_threads_amount.setText(_translate("mw_main", "Amount of threads:"))
        self.pb_cancel.setText(_translate("mw_main", "Cancel"))
        self.lb_message.setText(_translate("mw_main", "Message"))
        self.lb_ports_to_del.setText(_translate("mw_main", "Choose open ports:"))
        self.le_ports_to_del.setPlaceholderText(_translate("mw_main", "eg: 1, 2, 33, 456"))
        self.pb_close_selected.setText(_translate("mw_main", "Close selected ports"))
        self.pb_close_all.setText(_translate("mw_main", "Close all ports"))
        self.lb_found_ports.setText(_translate("mw_main", "Found open ports:"))
        self.pb_apply_to_scan.setText(_translate("mw_main", "Apply entries"))
        self.pb_clean_entries.setText(_translate("mw_main", "Clean entries"))
        self.lb_or.setText(_translate("mw_main", "or"))
