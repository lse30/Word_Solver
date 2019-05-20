import time

def main():
    start_time = time.time()

    from nltk.corpus import words
    word_list = words.words()
    letters = "l e s a t i d z n".split()
    letter_dict = dict()


    for letter in letters:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1




    output = []
    for word in word_list:
        i = 0
        possible = True
        while i < len(word) and possible:
            if word[i] not in letters:
                possible = False
            i += 1
        if possible:
            output.append(word)
    results = []
    for word in output:
        placeholder = []
        j = 0
        double = False
        while j < len(word) and not double:
            if word[j] in placeholder:
                double = True
                legal = check_word(letter_dict, word)
            else:
                placeholder.append(word[j])
            j += 1

        if not double or legal:
            results.append(word)

    results = sorted(results, key=len)

    if len(results) > 0:
        longest = len(results[-1])

    for word in results:
        if len(word) == longest:
            print(word)
    elapsed_time = time.time()
    print("Completed in {0:.2f} seconds".format(elapsed_time - start_time))



def check_word(letter_dict, word):
    output = True
    word_dict = dict()


    for letter in word:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1

    for key, value in word_dict.items():
        if value > letter_dict[key]:
            output = False

    return output


main()