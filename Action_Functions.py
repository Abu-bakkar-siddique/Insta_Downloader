from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()

# Create the main vertical layout
layout = QVBoxLayout(window)

# Create the textbox
textbox = QLineEdit()
layout.addWidget(textbox)

# Set the desired spaces to the right
spaces = 5

# Move the cursor to the right when the text is changed
def move_cursor():
    if len(textbox.text()) >= spaces:
        textbox.setCursorPosition(spaces)

textbox.textChanged.connect(move_cursor)

# Create the button
button = QPushButton("Button")
layout.addWidget(button)

window.show()
app.exec_()