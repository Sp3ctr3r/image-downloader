import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
import urllib.request
import os
import shutil
import string
import random
import time

font = QFont("Century Gothic",20)
font2 = QFont("Century Gothic",14)

class pencere(QWidget):
    def __init__(self):
        super().__init__()

        dikey = QVBoxLayout()

        self.setWindowTitle("Fotoğraf İndirici")

        #guide rehber demek
        self.guide = QLabel("Resim adresini nasıl alabilirim?")
        self.guide.setFont(font2)
        self.example = QLabel("Örnek : Google -> Bilgisayarlar -> Görseller -> \nHerhangi bir görselin üstüne sağ tık -> \nResim adresini kopyala")
        self.example.setFont(font2)

        self.data = QLineEdit()
        self.data.setFont(font)
        self.data.setPlaceholderText("İndirilecek resim adresi")

        self.down = QPushButton("İndir")
        self.down.setFont(font)
        self.down.clicked.connect(self.download)

        self.open = QPushButton("Klasöre Git")
        self.open.setFont(font)
        self.open.clicked.connect(self.Open)

        dikey.addWidget(self.guide)
        dikey.addWidget(self.example)
        dikey.addStretch()
        dikey.addWidget(self.data)
        dikey.addStretch()
        dikey.addWidget(self.down)
        dikey.addWidget(self.open)

        self.setLayout(dikey)
        self.setGeometry(450,200,350,400)
        self.show()

        try:
            os.mkdir(".\\Fotoğraflar")
            
        except FileExistsError:
            os.rename("Fotoğraflar","Fotoğraflar")

    def download(self):
        self.contentData = self.data.text()

        if self.contentData == "":
            mesaj = QMessageBox.information(self,"Hata!", "Lütfen adres girin", QMessageBox.Ok)

        else:
            self.down.setText("Fotoğraf indi")
            
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(5))
             
            urllib.request.urlretrieve(self.contentData, result_str + ".jpg")

            shutil.move(".\\" + result_str + ".jpg", ".\\Fotoğraflar")

            QTest.qWait(1000)
            
            self.down.setText("İndir")

    def Open(self):
        os.startfile(".\\Fotoğraflar")


uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())
