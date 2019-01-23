from PyQt5 import QtCore, QtGui, QtWidgets

class Dialogo(QtWidgets.QDialog):
    def init(self):
        QtWidgets.QDialog.init(self)
        self.resize(290, 290)
        self.setWindowTitle("¡¡ALERTA!!")
        self.etiqueta = QtWidgets.QLabel(self)