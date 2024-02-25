import json
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QInputDialog
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_notes()
        self.ui.notes.addItems(self.notes)
        self.ui.notes.itemClicked.connect(self.show_note)
        self.ui.save_note.clicked.connect(self.Savednote)
        self.ui.create_notes.clicked.connect(self.creatednote)
        self.ui.delete_notes.

    def show_note(self):
        self.name = self.ui.notes.selectedItems()[0].text()
        self.ui.text.setText(self.notes[self.name]["Текст"])

    def Savednote(self):
        self.notes[self.name] = {
                "Текст": self.ui.text.toPlainText(),
                "теги": []
            }
        with open("note.json", "w", encoding = "utf-8") as file:
            json.dump(self.notes, file)
        self.ui.notes.clear()
        self.ui.notes.addItems(self.notes)
        

    def clearnote(self):
        self.ui.text.clear()

    def creatednote(self):
        self.clearnote()
        note_name, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            self.name = note_name

    def read_notes(self):
        try:
            with open("note.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                    "Перша замітка":{
                        "Текст": "Це текст",
                        "теги": []
                    }
                }

    def deletenote(self):
        try:
            del self.notes[self.name]
            self.clearnote()
            self.ui.notes.clear()
            self.ui.notes.addItems(self.notes)
            self.Savednote()
        except:
            print("Помилка видалення")
        



            



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()