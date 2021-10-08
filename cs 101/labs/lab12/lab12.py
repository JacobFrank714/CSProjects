import string
import operator


def read_file(filename):  # makes a list of all the words that are in the txt file
    remove = dict.fromkeys(map(ord, '\n' + string.punctuation))
    f_contents = []
    with open(filename) as inputfile:
        f = inputfile.read().replace('\n', ' ').translate(remove).lower()
        f = f.split(' ')
        for i in f:
            f_contents.append(i)
    return f_contents


def make_freq_of_words(file_contents):  # counts the frequency of words in the file
    word_freq = {}
    for word in file_contents:
        if len(word) > 3:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    word_freq_sorted = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    return word_freq_sorted


def output_menu(dic):  # prints the list of 10 most common words, how many unique words, and how many words only show up one time
    number_of_words = 0
    num_of_unique_words = 0
    for i in range(0, len(dic)):
        number_of_words += 1
        if dic[i][1] == 1:
            num_of_unique_words += 1
    print("Most frequently used words\n"
          "{:>2}{:>15}{:>19}\n"
          "{:=>36}".format('#', 'Word', 'Freq.', '='))  # prints the header
    for i in range(1, 11):  # prints the table of top ten most used words
        try:
            print("{:>2}{:>15}{:>19}".format(i, dic[i-1][0], dic[i-1][1]))
        except IndexError:
            break
    print('There are {} words that occur only once\n'
          'There are {} unique words in the document'.format(num_of_unique_words, number_of_words))  # how many unique words there are and how many words only used 1 time


if __name__ == "__main__":
    while True:
        try:  # looks to see if the file is there
            filename = input('Enter the name of the file to open ')
            contents = read_file(filename)
        except FileNotFoundError:
            print('Could not open file', filename,'\nPlease Try again\n')
        doc_word_freq = make_freq_of_words(contents)
        output_menu(doc_word_freq)
        break
