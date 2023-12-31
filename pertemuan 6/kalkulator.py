import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget, QSizePolicy
from PyQt5 import QtGui, QtCore

class KalkulatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setGeometry(100, 100, 400, 600)

        # Set maximum size
        self.setMaximumSize(341, 476)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_layout = QGridLayout(self.central_widget)
        self.central_widget.setStyleSheet("background-color: black;")

        self.label = QLabel(self.central_widget)
        self.label.setStyleSheet("font: 75 36pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.central_layout.addWidget(self.label, 0, 0, 1, 4)

        tombol = [
            ('+', 1, 3, 1, 1), ('-', 2, 3, 1, 1),
            ('*', 3, 3, 1, 1), ('/', 4, 3, 1, 1), ('=', 5, 3, 1, 1),
            ('Clear', 1, 0, 1, 2), ('7', 2, 0, 1, 1), ('8', 2, 1, 1, 1), ('9', 2, 2, 1, 1),
            ('4', 3, 0, 1, 1), ('5', 3, 1, 1, 1), ('6', 3, 2, 1, 1),
            ('1', 4, 0, 1, 1), ('2', 4, 1, 1, 1), ('3', 4, 2, 1, 1),
            ('0', 5, 0, 1, 2), ('.', 5, 2, 1, 1), ('Del', 1, 2, 1, 1),
        ]

        for teks_tombol, baris, kolom, rowspan, colspan in tombol:
            tombol = QPushButton(teks_tombol, self.central_widget)
            tombol.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            tombol.setStyleSheet(
                "QPushButton{font: 75 20pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255); border-radius:30px;}"
                "QPushButton:hover{background-color: rgb(52, 157, 77);}"
                "QPushButton:pressed{color: rgb(27, 0, 0);}"
            )
            tombol.clicked.connect(lambda _, teks=teks_tombol: self.handle_button_click(teks))
            self.central_layout.addWidget(tombol, baris, kolom, rowspan, colspan)

    def handle_button_click(self, teks_tombol):
        teks_saat_ini = self.label.text()
        if teks_tombol == 'Del':
            self.label.setText(teks_saat_ini[:-1])
        elif teks_tombol == 'Clear':
            self.label.setText('')
        elif teks_tombol == '=':
            self.hitung_hasil()
        else:
            self.label.setText(teks_saat_ini + teks_tombol)

    def hitung_hasil(self):
        ekspresi = self.label.text()
        try:
            hasil = eval(ekspresi)
            self.label.setText(str(hasil))
        except Exception as e:
            self.label.setText('Error')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = KalkulatorUI()
    jendela.show()
    sys.exit(app.exec_())
    