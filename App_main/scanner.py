import json
import os
import pathlib
import socket
import sys
import threading
from queue import Queue

import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from UI.ports_scan_ui import Ui_mw_main

'''
socket.AF_INET -> connection to the internet not unix
socket.SOCK_STREAM -> basically says we are using TCP instead of UDP
'''
class SocketMain(qtw.QMainWindow, Ui_mw_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# target = '127.0.0.1'  # '80.111.243.87'
# ports_amount = 10000
# threads_amount = 500


# ls_ports = list(range(1, ports_amount))
# q = Queue()
# open_ports = []
# ls_threads = []

# def port_scan(port):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((target, port))
#         return 1
#     except:
#         return 0


# def fill_queue(port_ls):
#     for x in port_ls:
#         q.put(x)

# fill_queue(ls_ports)


# def worker():
#     while not q.empty():
#         port  = q.get()
#         if port_scan(port):
#             print('port {} is open'.format(port))
#             open_ports.append(port)

# for _ in range(threads_amount):
#     thread = threading.Thread(target=worker)
#     ls_threads.append(thread)

# for ts in ls_threads:
#     ts.start()

# for tf in ls_threads:
#     tf.join()

# print('open ports are: ', open_ports)

# socket.shutdown()
# socket.close()






if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    wind = SocketMain()
    wind.show()
    sys.exit(app.exec())
