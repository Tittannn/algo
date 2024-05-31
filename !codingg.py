from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle

class Question():
    def __init__(self, Question, right_answer, wrong1, wrong2, wrong3):
        self.Question = Question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(
        Question('Official language of Brazil', 'Brazilian', 'Portuguese', 'English', 'Spanish'))
question_list.append(
        Question('Which color does not appear on the American flag?', "blue", 'green', 'yellow', 'black'))
question_list.append(
        Question('Yakult national house', "urasa", 'yurta', 'igloo', 'khata'))


app = QApplication([])

button_ok = QPushButton('Reply')
lb_Question = QLabel('The most difficult question in the world!')

Radiogroupbox = QGroupBox('Answer options')

rbtn_1 = QRadioButton("Option 1")
rbtn_1 = QRadioButton("Option 2")
rbtn_1 = QRadioButton("Option 3")
rbtn_1 = QRadioButton("Option 4")

Radiogroup = QButtonGroup
Radiogroup.addButton(rbtn_1)
Radiogroup.addButton(rbtn_2)
Radiogroup.addButton(rbtn_3)
Radiogroup.addButton(rbtn_4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans3.addWidget(rbtn_1)
layout_ans3.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addlayout(layout_ans2)
layout_ans2.addlayout(layout_ans3)

Radiogroupbox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Test results')
lb_result = QLabel('Are you right or not?')
lb_correct = QLabel('Answer will be here!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result 
layout_line3 = QHBoxLayout() # "Answer" button

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(Radiogroupbox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(button_ok, stretch=2)

layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addlayout(layout_line1, stretch=2)
layout_card.addlayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addlayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    Radiogroupbox.hide()
    AnsGroupBox.show()
    button_ok.setText('Next')

def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Reply')
    RadioGroup.setExclusive(False) # removed the restrictions so as to reset the radio button choice
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # returned the restrictions, now only one radio button can be selected


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    ''' the function writes the values of the question and answers to the corresponding widgets, 
    at the same time the answer options are distributed randomly'''
    shuffle(answers) # shuffled the list of buttons, now some random button is first in the list
    answers[0].setText(q.right_answer) # fill the first element of the list with the right answer, the rest with wrong ones
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # question
    lb_Correct.setText(q.right_answer) # reply
    show_question() # show question panel