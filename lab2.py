from PyQt5 import QtWidgets
import sys
import design  # Это наш конвертированный файл дизайна
import math
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна        
        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.clicked.connect(self.encode)
    def enter(self):
        self.string=self.lineEdit.text()
        string=self.string
        self.n=len(string)
        self.l=int(math.log(self.n,2))
        self.a=[]
        self.sum=0
        for counter in range(0,len(string)):
            if string[counter]=="1":
                self.a.append(counter)
                self.sum+=counter
        self.m=len(self.a)
        self.R=self.sum%self.n
        self.lineEdit_2.setText(str(self.m))
        self.lineEdit_3.setText(str(self.n))
        self.lineEdit_4.setText(str(self.l))
        
    def encode(self):
        self.binR=bin(self.R)[2:]
        self.lineEdit_6.setText(self.string+self.binR)
        self.lineEdit_5.setText(str(self.R))
        self.lineEdit_7.setText(self.string+self.binR)
        counter=1
        for a in self.a:
            self.comboBox.addItem("a"+str(counter)+"="+str(a))
            counter+=1
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()