from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class TextEditDemo(QWidget):
    def __init__(self,parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle('QTextEdit 例子')

        #定义窗口的初始大小
        self.resize(300,270)
        #创建多行文本框
        self.textEdit=QTextEdit()
        #创建两个按钮
        self.btnPress1=QPushButton('显示文本')
        self.btnPress2=QPushButton('显示HTML')
        self.clipboard = QApplication.clipboard()
        self.originalText = self.clipboard.text();
        self.originalImage = self.clipboard.image();
        #实例化垂直布局
        layout=QVBoxLayout()
        #相关控件添加到垂直布局中
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        #设置布局
        self.setLayout(layout)

        self.textEdit.textChanged.connect(self.printText)

    def printText(self):
        print(str(self.textEdit.toHtml()))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=TextEditDemo()
    win.show()
    sys.exit(app.exec_())