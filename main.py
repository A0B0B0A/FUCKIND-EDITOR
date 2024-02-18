import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {
            "Перша замітка":{
                "Текст": "Це текст",
                "теги": []
            }
        }
        self.ui.notes.addItems(self.notes)
        self.ui.notes.itemClicked.connect(self.show_note)
        self.ui.save_note.clicked.connect(self.Savednote)

    def show_note(self):
        self.name = self.ui.notes.selectedItems()[0].text()
        self.ui.text.setText(self.notes[self.name]["Текст"])

    def Savednote(self):
        self.notes[self.name] = self.ui.text.toPlainText()
        with open("note.json", "w", encoding = "utf-8") as file:
            json.dump(self.notes, file)
        



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()