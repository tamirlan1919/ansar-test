from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout,
                             QWidget, QMessageBox, QFileDialog)
from PyQt6.QtGui import QAction
import sys


class MyNoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Мои заметки')
        self.setGeometry(200, 200, 400, 300)

        self.text_edit = QTextEdit()  # Где можно писать

        self.save_button = QPushButton('Сохранить заметку')  # Кнопка
        self.save_button.clicked.connect(self.save_note)

        self.load_button = QPushButton('Загрузить заметку')  # Кнопка

        layout = QVBoxLayout()  # Ориентация
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)

        container = QWidget()  # Контайнер
        container.setLayout(layout)
        self.setCentralWidget(container)

    def save_note(self):
        file_dialog = QFileDialog.getSaveFileName(self, 'Сохранение', '', 'Text Files (*.txt)')
        file_path = file_dialog[0]
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())
            QMessageBox.information(self, 'Успешно', 'Заметка успешно сохранена')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyNoteApp()
    main_window.show()
    sys.exit(app.exec())
