import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class SearchBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Search")
        self.setGeometry(300, 300, 300, 100)

        # Create a widget to hold the layout
        widget = QWidget(self)
        self.setCentralWidget(widget)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a label for the search prompt
        prompt_label = QLabel("Search:")
        layout.addWidget(prompt_label)

        # Create a line edit for the main search input
        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        # Create a line edit for the additional input
        self.additional_input = QLineEdit()
        self.additional_input.setFixedWidth(200)  # Adjust the width as needed
        layout.addWidget(self.additional_input)

        # Set the layout of the widget
        widget.setLayout(layout)

        # Move the cursor to the main search input
        self.search_input.setFocus()

        # Connect a signal to handle the Enter key press on the main search input
        self.search_input.returnPressed.connect(self.handle_search)

    def handle_search(self):
        # Get the search query from the main search input
        search_query = self.search_input.text()
        print("Search query:", search_query)
        # Perform search or further processing


if __name__ == '__main__':
    app = QApplication(sys.argv)
    search_box = SearchBox()
    search_box.show()
    sys.exit(app.exec_())