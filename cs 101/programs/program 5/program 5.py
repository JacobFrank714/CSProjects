import os
import random


class Directory:
    def __init__(self, file_name='', num_words=None, question_number=0):
        self.file = file_name
        self.num_words = num_words
        self.question_number = question_number
        self.quiz_words = []
        self.file_contents = {}

    def main_menu(self, files):
        while True:
            try:
                print('Vocabulary Program')
                for i in range(0, len(files)):
                    if '.txt' in files[i]:
                        print('\t' + files[i])
                self.file = input('\nEnter which set you would like to quiz over from the list ')
                if self.file == 'q' or self.file == 'Q':
                    return self.file
                return self.file_open()
            except FileNotFoundError:
                print('Please enter a selection from the list\n')
                continue

    def file_open(self):
        file = open(self.file, 'r')
        for line in file:
            line = line.strip("\n").split(":")
            self.file_contents[line[0]] = line[1]
        file.close()

    def rand_word(self):
        i = 0
        while i != self.num_words:
            file_keys = get_list(self.file_contents)
            word = random.choice(file_keys)
            self.quiz_words.append(word)
            i += 1


class Quiz(Directory):

    def num_questions(self):
        while True:
            try:
                self.num_words = int(input('How many words in your quiz? ==> '))
                if self.num_words <= 0:
                    raise ValueError
                elif self.num_words > 10:
                    raise ValueError
                break
            except ValueError:
                print('Number must be greater than zero and less than or equal to 10')
                continue

    def question_tick(self):
        self.question_number += 1

    def question_reset(self):
        self.question_number = 0

    def quiz_question(self):
        while self.question_number < self.num_words:
            answer = input('#{}.  Enter a valid spanish phrase for {}: '.format(self.question_number + 1, self.quiz_words[self.question_number]))
            if answer == self.file_contents[self.quiz_words[self.question_number]]:
                print('Correct answer! Good work.')
                self.question_tick()
                return 'Correct'
            elif answer != self.file_contents[self.quiz_words[self.question_number]]:
                print('Incorrect, valid answer is {}'.format(self.quiz_words[self.question_number]))
                self.question_tick()
                return 'Incorrect'


def get_list(dic):
    return list(dic.keys())


if __name__ == '__main__':
    while True:
        contents = os.listdir()
        quiz = Quiz()
        vocab = quiz.main_menu(contents)
        if vocab == 'q' or vocab == 'Q':
            break
        quiz.file_open()
        quiz.num_questions()
        quiz.rand_word()
        correct = 0
        incorrect = 0
        while quiz.question_number < quiz.num_words:
            a = quiz.quiz_question()
            if a == 'Correct':
                correct += 1
            elif a == 'Incorrect':
                incorrect += 1
        print('You got {} out of {}, which is {:.2f}%'.format(correct, quiz.question_number, ((correct / quiz.question_number) * 100)))
        quiz.question_reset()
