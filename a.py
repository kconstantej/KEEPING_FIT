from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
class apli(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("guardar.ui",self)