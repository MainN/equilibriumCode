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
        self.pushButton_3.clicked.connect(self.decode)
        self.f=0
        self.J=0
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
    def decode(self):
        self.comboBox_2.clear()
        self.new_string=self.lineEdit_7.text()[:self.n]
        self.new_sum=0
        self.new_m=0
        self.new_a=[]
        self.new_R=0
        self.lineEdit_10.setText("0")
        self.J=0
        for counter in range(0,len(self.new_string)):
            if self.new_string[counter]=="1":
                self.new_a.append(counter)
                self.new_sum+=counter
        counter=1
        self.new_m=len(self.new_a)
        self.lineEdit_8.setText(str(self.new_m))

        for a in self.new_a:
            self.comboBox_2.addItem("a"+str(counter)+"="+str(a))
            counter+=1
        counter=1
        self.new_R=self.new_sum%self.n
        self.lineEdit_9.setText(str(self.new_R))
        self.new_binR=bin(self.new_R)[2:]
        self.change=0
        self.updatedR=self.lineEdit_7.text()[self.n:]
        if self.m-self.new_m==1:
            self.J=self.R-self.new_R
            self.J=self.J%self.n
            self.J=self.J%self.n
            self.change=1
        if self.new_m-self.m==1:
            self.J=self.new_R%self.n
            self.J=self.J-self.R
            self.J=self.J%self.n
            self.change=1
        self.lineEdit_11.setText(str(self.J))
        if self.J!=0:
            self.lineEdit_10.setText("1")
        for x in range(0,len(self.binR)):
            diff=int(self.binR[x])-int(self.updatedR[x])
            if diff!=0 and self.f==0:
                if self.change==1:
                    self.lineEdit_10.setText("2")
                    print("break")
                    break
                self.pos=x
                self.f=1
                self.lineEdit_10.setText("1")
                self.lineEdit_11.setText(str(self.n+self.pos))
                continue
            if diff!=0 and self.f!=0:
                self.lineEdit_10.setText("2")
        if self.lineEdit_10.text()=="1":
            dup=list(self.lineEdit_7.text())
            pos=int(self.lineEdit_11.text())
            print(type(dup))
            dup[pos]=str((int(dup[pos])+1)%2)
            if dup[pos]=="1":
                if self.m!=self.new_m:
                    self.lineEdit_10.setText("2")
            dup_string=""
            for x in dup:
                dup_string+=x
            self.lineEdit_12.setText(dup_string[:self.n])
        if self.lineEdit_10.text()=="2":
            if self.change==1:
                self.lineEdit_12.setText("Один информационный и один проверочный символы")
            else:
                self.lineEdit_12.setText("Симметричная ошибка в информационной части")
            self.lineEdit_11.setText("")
        if self.lineEdit_10.text()=="0":
            self.lineEdit_12.setText("")
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()