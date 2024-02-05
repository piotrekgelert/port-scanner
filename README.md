# port-scanner
Port scanner application made in python 3.12 with pyqt6.
Fast tool to help secure your computer.
It checks if you have any open unused port on your computer.


## ui examples
<p align="middle">
  <img src="https://github.com/piotrekgelert/port-scanner/blob/main/images/entry_image.png" width="30%"/>
  <img src="https://github.com/piotrekgelert/port-scanner/blob/main/images/prepared_to_scan.png" width="30%"/>
  <img src="https://github.com/piotrekgelert/port-scanner/blob/main/images/found_ports.png" width="30%"/>
</p>

### notes
- [x] scans ports of any given address
- [x] scans ports from the beginning to the chosen number or in given range
- [x] uses multithreading (faster scanning)

### used packages
- [PyQt6 6.6.1](https://www.riverbankcomputing.com/software/pyqt/)
- [pyinstaller 6.3.0](https://www.pyinstaller.org/)
- [auto-py-to-exe 2.42.0](https://github.com/brentvollebregt/auto-py-to-exe)


### running the project
App opens from `App_main/scanner.py`

### licence
This project is licensed under the [MIT] License - see [Licence.md](LICENSE)
file for details.