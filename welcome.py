# -*- coding: utf-8 -*-

"""
Module implementing WelcomWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from main import MainWindow

from Ui_welcome import Ui_WelcomWindow


class WelcomWindow(QMainWindow, Ui_WelcomWindow):

    panel = None
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(WelcomWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.panel = MainWindow()
        self.panel.show()
        self.close()
        return
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = WelcomWindow()
    dlg.show()
    sys.exit(app.exec_())
