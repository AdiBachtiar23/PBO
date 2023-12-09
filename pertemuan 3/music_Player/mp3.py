import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtCore import Qt, QUrl  
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class MP3Player(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MP3 Player')
        self.setGeometry(100, 100, 400, 200)

        self.player = QMediaPlayer()

        self.label = QLabel('Pilih file MP3', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.btn_open = QPushButton('Pilih File', self)
        self.btn_open.clicked.connect(self.open_file)

        self.btn_play = QPushButton('Mainkan', self)
        self.btn_play.clicked.connect(self.play_music)

        self.btn_stop = QPushButton('Hentikan', self)
        self.btn_stop.clicked.connect(self.stop_music)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_stop)

        self.setLayout(layout)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Pilih File MP3', '', 'MP3 Files (*.mp3);;All Files (*)', options=options)

        if file_name:
            self.label.setText(f'Sedang memutar: {file_name}')
            content = QMediaContent(QUrl.fromLocalFile(file_name))
            self.player.setMedia(content)
    
    def play_music(self):
        self.player.play()

    def stop_music(self):
        self.player.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mp3_player = MP3Player()
    mp3_player.show()
    sys.exit(app.exec_())
