import sys
from gui import Ui_Form
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
import Utoutou

class mywindow(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def run(self):
        size = int(self.lineEdit.text())
        houzhui = self.lineEdit_2.text()
        if houzhui == '':
            Utoutou.run_app(size)
        else:
            Utoutou.run_app(size, houzhui)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())