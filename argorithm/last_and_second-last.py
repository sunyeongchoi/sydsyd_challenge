def lastLetters(word):
    str_to_list = list(word)[-2:]
    return ' '.join(str_to_list[::-1])


if __name__ == '__main__':
    real_answer = lastLetters('bat')
    print(real_answer)
