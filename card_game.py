from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Информатика-331-4\AppData\Local\Programs\Python\Python39\Lib\site-packages\PyQt5\Qt5\plugins\platforms'


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.questions = [
            {
                'question': "Какой язык программирования чаще всего используется для веб-разработки?",
                'answers': ["Ruby", "JavaScript", "C++", "Python"],
                'correct': "JavaScript"
            },
            {
                'question': "Что такое переменная в программировании?",
                'answers': ["Устройство для ввода", "Имя для хранения данных", "Тип ошибки", "Название функции"],
                'correct': "Имя для хранения данных"
            },
            {
                'question': "Что делает оператор if?",
                'answers': ["Повторяет блок кода", "Выполняет блок кода при условии", "Определяет функцию", "Завершает программу"],
                'correct': "Выполняет блок кода при условии"
            },
            {
                'question': "Что такое цикл for?",
                'answers': ["Команда для выбора", "Команда для повторения кода", "Ошибка компиляции", "Переменная"],
                'correct': "Команда для повторения кода"
            },
            {
                'question': "Какой из этих языков является языком программирования общего назначения?",
                'answers': ["HTML", "CSS", "Java", "SQL"],
                'correct': "Java"
            },
            {
                'question': "Что такое функция в программировании?",
                'answers': ["Ключевое слово", "Повторяющийся код", "Блок кода, который выполняет задачу", "Ошибка"],
                'correct': "Блок кода, который выполняет задачу"
            },
            {
                'question': "Что означает аббревиатура IDE?",
                'answers': ["Interface Development Environment", "Integrated Development Environment", "Internal Data Entry", "Internet Development Engine"],
                'correct': "Integrated Development Environment"
            },
            {
                'question': "Какой из этих типов данных предназначен для хранения логических значений?",
                'answers': ["String", "Boolean", "Integer", "Float"],
                'correct': "Boolean"
            },
            {
                'question': "Что такое массив?",
                'answers': ["Множество данных одного типа в одной структуре", "Отдельная переменная", "Функция", "Ошибка"],
                'correct': "Множество данных одного типа в одной структуре"
            }
        ]

        self.current_question = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("квиз по программированию")
        self.setGeometry(100, 100, 400, 200)

        self.RadioGroupBox = QGroupBox("Варианты ответов")
        self.rbtn_1 = QRadioButton()
        self.rbtn_2 = QRadioButton()
        self.rbtn_3 = QRadioButton()
        self.rbtn_4 = QRadioButton()
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(True)

        self.buttonGroup.addButton(self.rbtn_1)
        self.buttonGroup.addButton(self.rbtn_2)
        self.buttonGroup.addButton(self.rbtn_3)
        self.buttonGroup.addButton(self.rbtn_4)

        self.layout_ans1 = QHBoxLayout()   
        layout_ans2 = QVBoxLayout()
        layout_ans3 = QVBoxLayout()

        layout_ans2.addWidget(self.rbtn_1)
        layout_ans2.addWidget(self.rbtn_2)
        layout_ans3.addWidget(self.rbtn_3)
        layout_ans3.addWidget(self.rbtn_4)
        self.layout_ans1.addLayout(layout_ans2)
        self.layout_ans1.addLayout(layout_ans3)
        self.RadioGroupBox.setLayout(self.layout_ans1)

        self.result_text_label = QLabel("") 
        self.layout_ans1.addWidget(self.result_text_label)

        self.btn = QPushButton("Проверить")
        self.btn.clicked.connect(self.on_click)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        main_layout = QVBoxLayout()
        self.question_label = QLabel("")
        main_layout.addWidget(self.question_label)
        main_layout.addWidget(self.RadioGroupBox)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.btn)

        self.setLayout(main_layout)

        self.show_question()

    def show_question(self):
        q = self.questions[self.current_question]
        #self.RadioGroupBox.setExcl
        self.question_label.setText(q['question'])
        self.rbtn_1.setText(q['answers'][0])
        self.rbtn_2.setText(q['answers'][1])
        self.rbtn_3.setText(q['answers'][2])
        self.rbtn_4.setText(q['answers'][3])
        self.rbtn_1.setChecked(False)
        self.rbtn_2.setChecked(False)
        self.rbtn_3.setChecked(False)
        self.rbtn_4.setChecked(False)
        self.rbtn_1.show()
        self.rbtn_2.show()
        self.rbtn_3.show()
        self.rbtn_4.show()
        self.result_text_label.setText("")
        self.btn.setText("Проверить")

    def on_click(self):
        if self.btn.text() == "Проверить":
            q = self.questions[self.current_question]
            chosen = None
            if self.rbtn_1.isChecked():
                chosen = self.rbtn_1.text()
            elif self.rbtn_2.isChecked():
                chosen = self.rbtn_2.text()
            elif self.rbtn_3.isChecked():
                chosen = self.rbtn_3.text()
            elif self.rbtn_4.isChecked():
                chosen = self.rbtn_4.text()

            if chosen:
                if chosen == q['correct']:
                    self.result_text_label.setText("Вы ответили правильно!")
                else:
                    self.result_text_label.setText(f"Неправильно!")
                self.rbtn_1.hide()
                self.rbtn_2.hide()
                self.rbtn_3.hide()
                self.rbtn_4.hide()
                self.btn.setText("Следующий вопрос")
            else:
                self.result_text_label.setText("Пожалуйста, выберите вариант ответа")
        elif self.btn.text() == "Следующий вопрос":
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.show_question()
            else:
                self.result_text_label.setText("Викторина завершена!")
                self.btn.setDisabled(True)

app = QApplication([])
window = ExampleApp()
window.show()
app.exec()
