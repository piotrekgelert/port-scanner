import json
import os
import pathlib
import socket
import sys
import threading
from queue import Queue
from threading import Thread
from typing import Any, Iterable

import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from UI.ports_scan_ui import Ui_mw_main  # type: ignore

'''
socket.AF_INET -> connection to the internet not unix
socket.SOCK_STREAM -> basically says we are using TCP instead of UDP
'''
class SocketMain(qtw.QMainWindow, Ui_mw_main):
    q: Queue = Queue()
    open_ports: list[Any] = []
    threads_ls: list[Thread]= []

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pb_apply_to_scan.clicked.connect(self.apply_queue)
        self.pb_scan.clicked.connect(self.scan_ports)
        self.pb_clean_entries.clicked.connect(self.clean_entries)
        self.pb_close_selected.clicked.connect(self.close_selected)
        self.pb_cancel.clicked.connect(self.close)
    
    def port_scanner(self, port) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.le_target_port.text(), port))
            return True
        except:
            return False
    
    def fill_queue(self, ports_ls:Iterable[int]) -> None:
        for x in ports_ls:
            self.q.put(x)
    
    def apply_queue(self) -> None:
        self.fill_queue(list(range(1, int(self.le_ports_amount.text()))))
    
    def worker(self) -> None:
        while not self.q.empty():
            port: Any = self.q.get()
            if self.port_scanner(port):
                self.open_ports.append(port)
    
    def scan_ports(self) -> Any:
        self.lb_message.setText('Ports are being scanned, wait until finished')
        for _ in range(int(self.le_threads_amount.text())):
            thread: Thread = Thread(target=self.worker)
            self.threads_ls.append(thread)
        
        for ts in self.threads_ls:
            ts.start()

        for tf in self.threads_ls:
            tf.join()
        
        self.lb_le_found_ports.setText(str(self.open_ports)[1:-1])
        self.lb_message.clear()
    
    def clean_entries(self) -> None:
        self.le_target_port.clear()
        self.le_threads_amount.clear()
        self.le_ports_amount.clear()
        self.threads_ls.clear
    
    def close_all(self) -> Any:
        for op in self.open_ports:
            try:
                sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.le_target_port.text(), op))
                sock.shutdown(1)
                sock.close()
            except:
                print(f'socket: {op} didn\'t close')
    
    def close_selected(self) -> Any:
        for op in self.le_ports_to_del.text().split(','):
            try:
                sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.le_target_port.text(), int(op.strip())))
                sock.shutdown(1)
                sock.close()
            except:
                print(f'socket: {op.strip()} didn\'t close')

    def disconnect_selected(self):
        ...





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
