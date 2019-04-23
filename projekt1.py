# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:08:12 2019
@author: Klaudia
"""

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton('Oblicz punkt przecięcia i narysuj wykres', self)
        self.clrChoose=QPushButton('Wybierz kolor odcinka CD', self)
        self.clrChoose2=QPushButton('Wybierz kolor odcinka AB', self)
        self.wyczysc = QPushButton('wyczysc',self)
        self.polecenie=QLabel("Wprowadź współrzędne:")

        self.xalabel = QLabel("Xa", self)
        self.xaEdit = QLineEdit()
        self.yalabel = QLabel("Ya", self)
        self.yaEdit = QLineEdit()
        
        self.xblabel = QLabel("Xb", self)
        self.xbEdit = QLineEdit()
        self.yblabel = QLabel("Yb", self)
        self.ybEdit = QLineEdit()
        
        self.xclabel = QLabel("Xc", self)
        self.xcEdit = QLineEdit()
        self.yclabel = QLabel("Yc", self)
        self.ycEdit = QLineEdit()
        
        self.xdlabel = QLabel("Xd", self)
        self.xdEdit = QLineEdit()
        self.ydlabel = QLabel("Yd", self)
        self.ydEdit = QLineEdit()
        
        self.xplabel = QLabel("Xp", self)
        self.xpEdit = QLineEdit()
        self.yplabel = QLabel("Yp", self)
        self.ypEdit = QLineEdit()
        
        self.punktEdit = QLineEdit() 
        
        #apka
    
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
    
        layout = QGridLayout(self)
        layout.addWidget(self.xalabel, 8, 7)
        layout.addWidget(self.xaEdit, 9, 7)
        layout.addWidget(self.yalabel, 8, 8)
        layout.addWidget(self.yaEdit, 9, 8)
        
        layout.addWidget(self.xblabel, 10, 7)
        layout.addWidget(self.xbEdit, 11, 7)
        layout.addWidget(self.yblabel, 10, 8)
        layout.addWidget(self.ybEdit, 11, 8)
    
        layout.addWidget(self.xclabel, 12, 7)
        layout.addWidget(self.xcEdit, 13, 7)
        layout.addWidget(self.yclabel, 12, 8)
        layout.addWidget(self.ycEdit, 13, 8)
        
        layout.addWidget(self.xdlabel, 14, 7)
        layout.addWidget(self.xdEdit, 15, 7)
        layout.addWidget(self.ydlabel, 14, 8)
        layout.addWidget(self.ydEdit, 15, 8)
        
        layout.addWidget(self.xplabel, 18, 7)
        layout.addWidget(self.xpEdit, 19, 7)
        layout.addWidget(self.yplabel, 18, 8)
        layout.addWidget(self.ypEdit, 19, 8)
        
        #przycisk oblicz
        layout.addWidget(self.button,17, 7, 1, 2)
        #okienko lokaliacji punktu 
        layout.addWidget(self.punktEdit, 21, 5, 1, 7)
        #polozenie wykresu
        layout.addWidget(self.canvas, 1,7,7,7)
        #polozenie napisu "Wprowadź wspolrzedne"
        layout.addWidget(self.polecenie,8,5)
        #polozenie przyciskow kolorów
        layout.addWidget(self.clrChoose, 6, 2, 1, 4)
        layout.addWidget(self.clrChoose2, 5, 2, 1, 4)
        #polozenie przycisku wyczysc
        layout.addWidget(self.wyczysc, 4,2,1,4)
        
        #polaczenie przycisku singal z akcja slot
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        self.clrChoose2.clicked.connect(self.clrChooseF2)
        self.wyczysc.clicked.connect(self.wyczysc1)
        
    def checkValues(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus()
            return None
        
        
    def clrChooseF(self):
        self.color = QColorDialog.getColor()
        if  self.color2.name() == "#000000":
            self.rysuj(col=self.color.name())
        elif self.color.name() == "#000000":
            self.rysuj(col2=self.color2.name())
        elif self.color.name() != "#000000" and self.color2.name() != "#000000":
            self.rysuj(col=self.color.name(), col2=self.color2.name())
        else:
            pass
    
    def clrChooseF2(self):
        self.color2 = QColorDialog.getColor()
        if self.color.isValid() and self.color2.isValid():
            self.rysuj(col=self.color.name(), col2=self.color2.name())
        elif self.color.isValid() == False and self.color2 != None:
            self.rysuj(col2=self.color2.name())
        elif self.color.isValid() == False and self.color != None:
            self.rysuj(col=self.color.name())
        else:
            pass
        
    def handleButton(self):
        self.rysuj()
        
    def wyczysc1(self):
        self.xaEdit.setText('')
        self.yaEdit.setText('')
        self.xbEdit.setText('')
        self.ybEdit.setText('')
        self.xcEdit.setText('')
        self.ycEdit.setText('')
        self.xdEdit.setText('')
        self.ydEdit.setText('')
        self.punktEdit.setText('')
        self.figure.clear()
        self.canvas.draw()
            
    def rysuj(self, col='r', col2='blue'):
        Xa = self.checkValues(self.xaEdit)
        Ya = self.checkValues(self.yaEdit)
        Xb = self.checkValues(self.xbEdit)
        Yb = self.checkValues(self.ybEdit)
        Xc = self.checkValues(self.xcEdit)
        Yc = self.checkValues(self.ycEdit)
        Xd = self.checkValues(self.xdEdit)
        Yd = self.checkValues(self.ydEdit)
        
        
        if Xa or Xb or Xc or Xd !=None and Ya or Yb or Yc or Yd != None: 
            self.figure.clear() #czyszczenie pozsotałowsci
            ax = self.figure.add_subplot(111)
            self.canvas.draw()
        else:
            msg_err = QMessageBox()
            msg_err.setWindowTitle("Komunikat")
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText("Podałes błędne współrzędne!")
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
            
        dXab = Xb - Xa
        dYab = Yb - Ya
        dXcd = Xd - Xc
        dYcd = Yd - Yc
        dXac = Xc - Xa
        dYac = Yc - Ya
        x = dXab*dYcd - dYab*dXcd    
            
         
        if x!= 0:
            t1 = (dXac*dYcd - dYac*dXcd)/x
            t2 = (dXac*dYab - dYac*dXab)/x
            if t1>=0 and t1<=1 and t2>=0 and t2<=1:
                xp = Xa + t1*dXab
                yp = Ya + t1*dYab
                a = "{0:.3f}".format(xp)
                b = "{0:.3f}".format(yp)
                self.xpEdit.setText(str(a))
                self.ypEdit.setText(str(b))
                self.punktEdit.setText(str("Punkt P znajduje się na przecięciu odcinków"))
            elif 0 <= t1 <=1:
                xp = Xa + t1*dXab
                yp = Ya + t1*dYab
                c = "{0:.3f}".format(xp)
                d = "{0:.3f}".format(yp)
                self.xpEdit.setText(str(c))
                self.ypEdit.setText(str(d))
                self.punktEdit.setText(str("Punkt P znajduje się na przedłużeniu odcinka cd"))
                
            elif 0 <= t2 <=1:
                xp = Xa + t1*dXab
                yp = Ya + t1*dYab
                e = "{0:.3f}".format(xp)
                f = "{0:.3f}".format(yp)
                self.xpEdit.setText(str(e))
                self.ypEdit.setText(str(f))
                self.punktEdit.setText(str("Punkt P znajduje się na przedłużeniu odcinka ab"))
            else:
                xp = Xa + t1*dXab
                yp = Ya + t1*dYab
                g = "{0:.3f}".format(xp)
                h = "{0:.3f}".format(yp)
                self.xpEdit.setText(str(g))
                self.ypEdit.setText(str(h))
                self.punktEdit.setText(str("Punkt P znajduje się na przedłużeniu obu odcinków"))
        elif x == 0:
            self.punktEdit.setText(str("Brak punktu P, odcinki są równoległe"))
            
                             
        #zapis do pliku
        plik = open('mojpliktekstowy.txt','w')
        plik.write("|{:^15}|{:^15}|{:^15}|\n".format("Nazwa punktu", "X[m]", "Y[m]" ))
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("A",Xa, Ya)) 
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("B",Xb, Yb))
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("C",Xc, Yc))
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("D",Xd, Yd))
        
        if self.xaEdit == None:
            plik.write("|{:^15.3f}|{:^15.3f}|{:^15.3f}|\n".format("P","brak", "brak"))
        else:
            plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("P", xp, yp))
        plik.close()
       
        #wykres 
        self.figure.clear() #czyszczenie 
        ax = self.figure.add_subplot(111)
        ax.plot([yp, Yb], [xp, Xb], 'go:')
        ax.plot([Ya, yp], [Xa, xp], 'go:')
        ax.plot([yp, Yd], [xp, Xd], 'go:')
        ax.plot([Yc, yp], [Xc, xp], 'go:')
        ax.plot([Ya, Yb], [Xa, Xb], color=col2, marker ='o')
        ax.plot([Yc, Yd], [Xc, Xd], color=col, marker ='o')
        ax.plot(yp, xp, color= 'blue', marker= 'o')
        
        #etykiety na wykresie, rozmiar i kolor dla każdego punktu
        ax.text(Ya, Xa, " A(" + str(Xa) +","+ str(Ya)+")", fontsize = 7, color = "black")
        ax.text(Yb, Xb, " B(" + str(Xb) +","+ str(Yb)+")", fontsize = 7, color = "black")
        ax.text(Yc, Xc, " C(" + str(Xc) +","+str(Yc)+")", fontsize = 7, color = "black")
        ax.text(Yd, Xd, " D(" + str(Xd) +","+ str(Yd)+")", fontsize = 7, color = "black")
        ax.text(yp, xp, " P(" + str(xp) +","+str(yp)+")", fontsize = 7, color = "black")
        self.canvas.draw()
            
if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    window = Window()
    window.show()
    sys.exit(app.exec_())