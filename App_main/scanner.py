import json
import os
import pathlib
import socket
import sys
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
        self.pb_cancel.clicked.connect(self.close)
        Messages.entry_message(self)
    
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
        if len(
            self.le_target_port.text()
            ) and len(
                self.le_ports_amount.text()
                ) and len(
                    self.le_threads_amount.text()
                ):
            if '-' in self.le_ports_amount.text():
                n1, n2 = [int(x) for x in self.le_ports_amount.text().split('-')]
                self.fill_queue(list(range(n1, n2)))
            else:
                self.fill_queue(list(range(1, int(self.le_ports_amount.text()))))
            Messages.apply(self)
        else:
            Messages.forgotten_entries(self)
    
    def worker(self) -> None:
        while not self.q.empty():
            port: Any = self.q.get()
            if self.port_scanner(port):
                self.open_ports.append(port)
    
    def scan_ports(self) -> Any:
        for _ in range(int(self.le_threads_amount.text())):
            thread: Thread = Thread(target=self.worker)
            self.threads_ls.append(thread)
        
        for ts in self.threads_ls:
            ts.start()

        for tf in self.threads_ls:
            tf.join()
        
        self.lb_le_found_ports.setText(str(self.open_ports)[1:-1])
        Messages.clean(self)
 
    def clean_entries(self) -> None:
        self.le_target_port.clear()
        self.le_threads_amount.clear()
        self.le_ports_amount.clear()
        self.threads_ls.clear()



class Messages(SocketMain):
    def entry_message(self):
        self.lb_message.setText(
            'Fill entries:\n "{}", "{}", "{}" \nand push "{}" button'.format(
                self.lb_target_port.text()[:-1],
                self.lb_ports_amount.text()[:-1],
                self.lb_threads_amount.text()[:-1],
                self.pb_apply_to_scan.text()
            )
        )    
    
    def forgotten_entries(self):
        self.lb_message.setText(
                'All entries:\n"{}", "{}" and "{}"\n have to be filled in'.format(
                    self.lb_target_port.text()[:-1],
                    self.lb_ports_amount.text()[:-1],
                    self.lb_threads_amount.text()[:-1]
                )
            )
    
    def apply(self):
        self.lb_message.setText(
                'Now push "{}" button'.format(
                    self.pb_scan.text()))
    
    def clean(self):
        self.lb_message.clear()





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    wind = SocketMain()
    wind.show()
    sys.exit(app.exec())
