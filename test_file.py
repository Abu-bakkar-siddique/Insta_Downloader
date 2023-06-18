import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout, QPushButton
from PyQt5 import QtCore

class CenteredButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centered Button Example")
        self.setGeometry(300, 200, 400, 300)  # Set the initial window size and position

        # Create a central widget and set it as the main window's central widget
        central_widget1 = QWidget(self)
        self.setCentralWidget(central_widget1)

        # Create a vertical layout manager
        layout = QHBoxLayout(central_widget1)
        
        # Create the button and add it to the layout
        button = QPushButton("Centered Button")
        button.setFixedSize(100,30)
        layout.addWidget(button)

        #creating buttons
        button1 = QPushButton("Download Highlights")
        button1.setFixedSize(180,30)
        button1.setStyleSheet("QPushButton { background-color: red; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-family: Arial; }"
                      "QPushButton:hover { background-color: black; }")
        layout.addWidget(button1)
        # Set the layout alignment to center
        layout.setAlignment(QtCore.Qt.AlignCenter)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CenteredButtonWindow()
    window.show()
    sys.exit(app.exec_())
    