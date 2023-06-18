import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class App(QMainWindow):
    def __init__ (self):
        super().__init__()
        #creating a window        
        self.setWindowTitle("Bulk Downloader for Instagram")
        self.setGeometry(300,300,300,300)
        #self.setStyleSheet("background-color:black;")


    def add_buttons(self):
       
        #creating a widget
        C_widget = QWidget(self)
        self.setCentralWidget(C_widget)
        layoutB = QHBoxLayout(C_widget)
        #creating the buttons
        button1 = QPushButton("Download Heighlights")
        button1.setStyleSheet("QPushButton { background-color: red; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-family: Arial; }"
                  "QPushButton:hover { background-color: black; }")
        button1.setFixedSize(180,50)
        button1.setFont(QFont("Arial",10))
        button2 = QPushButton("Download Stories")
        button2.setStyleSheet("QPushButton { background-color: red; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-family: Arial; }"
                  "QPushButton:hover { background-color: black; }")
        button2.setFixedSize(150,50)     
        button2.setFont(QFont("Arial",10))
        button3 = QPushButton("Download profile")
        button3.setStyleSheet("QPushButton { background-color: red; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-family: Arial; }"
                  "QPushButton:hover { background-color: black; }")         
        button3.setFixedSize(150,50) 
        button3.setFont(QFont("Arial",10))      
        button4 = QPushButton("Download IGTV")
        button4.setStyleSheet("QPushButton { background-color: red; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-family: Arial; }"
                  "QPushButton:hover { background-color: black; }")
        button4.setFixedSize(150,50)       
        button4.setFont(QFont("Arial",10))
        #adding buttons to the layout
        layoutB.addWidget(button1)  
        layoutB.addWidget(button2) 
        layoutB.addWidget(button3)  
        layoutB.addWidget(button4)
        # Set the layout alignment to center
        layoutB.setAlignment(QtCore.Qt.AlignCenter)

    #mathod to create inputBox
    def input_box(self):
        self.textbox = QLineEdit(self)
        self.textbox.setCursorPosition(44) 
        self.textbox.setStyleSheet("border: 2px solid black; border-radius: 15px;")
        self.textbox.move(505, 230)
        self.textbox.resize(300,50)
        self.textbox.setFont(QFont("Arial", 12))
        self.textbox.setCursorPosition(44) 
        self.textbox.setPlaceholderText("          paste the Instagram user name")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    x = App()
    x.add_buttons()
    x.input_box()
    x.show()
    sys.exit(app.exec_())
