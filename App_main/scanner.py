import re
import socket
import sys
from queue import Queue
from threading import Thread
from typing import Any, Iterable

import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from UI.ports_scan_ui import Ui_mw_main  # type: ignore

'''
socket.AF_INET -> connection to the internet not unix
socket.SOCK_STREAM -> basically says we are using TCP instead of UDP
'''
class SocketMain(qtw.QMainWindow, Ui_mw_main):
    q: Queue = Queue()
    open_ports: list[Any] = []
    threads_ls: list[Thread]= []
    threads_nb: int = 0
    applied_ports: bool = False
    applied_threads: bool = False

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.tips_style()
        self.pb_apply_to_scan.clicked.connect(self.apply_queue)
        self.pb_scan.clicked.connect(self.scan_ports)
        self.pb_clean_entries.clicked.connect(self.clean_entries)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_clean_ports.clicked.connect(self.clean_open_ports)
        self.lb_le_found_ports.setWordWrap(True)
        Messages.entry_message(self)
    
    def tips_style(self):
        self.lb_scanned_ports_tip.setStyleSheet(
            "QLabel {color: rgb(150, 150, 150); font: 10pt 'Comic Sans MS'}"
        )
        self.lb_threads_tip.setStyleSheet(
            "QLabel {color: rgb(150, 150, 150); font: 10pt 'Comic Sans MS'}"
        )
    
    def port_scanner(self, port) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.1', port))
            return True
        except:
            return False
    
    def fill_queue(self, ports_ls:Iterable[int]) -> None:
        for x in ports_ls:
            self.q.put(x)
    
    def validate_input(self, txt: str) -> bool:
        ls_punct = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', 
                    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
                    '^', '_', '`', '{', '|', '}', '~']
        r = re.compile('[' + 'a-zA-Z' + re.escape(''.join(ls_punct)) + ']')
        res = bool(re.findall(r, txt)) or bool(re.match('[-0]', txt))
        return not res
    
    def _ports_limit(self) -> None:
        n, n1, n2 = 0, 0, 0
        if len(self.le_ports_amount.text())\
            and self.validate_input(self.le_ports_amount.text()):
            if '-' in self.le_ports_amount.text():
                n1, n2 = [
                    int(x) for x in self.le_ports_amount.text().split('-')
                    ]
                if n1 > 65536 or n2 > 65536:
                    pass
                else:
                    self.fill_queue(list(range(n1, n2)))
            else:
                n = int(self.le_ports_amount.text())
                if n > 65536:
                    pass
                else:
                    self.fill_queue(list(range(1, n)))
            
            if n1 > 65536 or n2 > 65536 or n > 65536:
                Messages.exceed_ports_limit(self)
            else:
                self.applied_ports = True
                Messages.apply(self)
        else:
            self.le_ports_amount.clear()
            Messages.forgotten_entries(self)
    
    def _threads_limit(self) -> None:
        if len(self.le_threads_amount.text())\
            and self.validate_input(self.le_threads_amount.text()):
            self.threads_nb  = int(self.le_threads_amount.text())
            if self.threads_nb > 500:
                Messages.exceed_threads_limit(self)
            else:
                self.applied_threads = True
        else:
            self.le_threads_amount.clear()
            Messages.forgotten_entries(self)

    def apply_queue(self) -> None:
        self._ports_limit()
        self._threads_limit()
    
    def worker(self) -> None:
        while not self.q.empty():
            port: Any = self.q.get()
            if self.port_scanner(port):
                self.open_ports.append(port)
    
    def scan_ports(self) -> Any:
        if self.applied_ports == True and self.applied_threads == True:
            for _ in range(self.threads_nb):
                thread: Thread = Thread(target=self.worker)
                self.threads_ls.append(thread)
            
            for ts in self.threads_ls:
                ts.start()

            for tf in self.threads_ls:
                tf.join()
            
            self.lb_le_found_ports.setText(str(self.open_ports)[1:-1])
            self.pb_apply_to_scan.setDisabled(True)
            self.pb_scan.setDisabled(True)
            Messages.scan_again(self)
        else:
            Messages.forgotten_entries(self)

    def clean_entries(self) -> None:
        self.le_threads_amount.clear()
        self.le_ports_amount.clear()
        self.threads_ls.clear()
        self.applied_ports = False
        self.applied_threads = False
        self.pb_apply_to_scan.setDisabled(False)
        self.pb_scan.setDisabled(False)
        Messages.clean(self)

    
    def clean_open_ports(self) -> None:
        self.lb_le_found_ports.clear()



class Messages(SocketMain):
    def entry_message(self):
        self.lb_message.setText(
            'Fill entries:\n"{}", "{}" and click on \n"{}" button'.format(
                self.lb_ports_amount.text()[:-1],
                self.lb_threads_amount.text()[:-1],
                self.pb_apply_to_scan.text()
            )
        )    
    
    def forgotten_entries(self):
        self.lb_message.setText(
                'Entries:\n"{}" and "{}"\n have to be filled in with positive'
                ' integers only, next click on \n"{}" button'.format(
                    self.lb_ports_amount.text()[:-1],
                    self.lb_threads_amount.text()[:-1],
                    self.pb_apply_to_scan.text()
                )
            )
    
    def apply(self):
        self.lb_message.setText(
                'Now click on "{}" button'.format(
                    self.pb_scan.text()))
    
    def clean(self):
        self.lb_message.clear()
    
    def exceed_ports_limit(self):
        self.lb_message.setText(
            'The provided number of ports is bigger then max. number of ports'
            )
    
    def exceed_threads_limit(self):
        self.lb_message.setText(
            'The provided number of threads is'
            ' bigger then max. number of threads'
            )
    def scan_again(self):
        self.lb_message.setText(
            'Scan completed. If you want to scan again,'
            ' first click on\n"{}" button'.format(
                self.pb_clean_entries.text()
            )
        )



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    wind = SocketMain()
    wind.show()
    sys.exit(app.exec())
