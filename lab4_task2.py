def get_count_char(str_):
    str_ = str_.lower()
    str_list = str_.split(" ")
    str_list.sort()
    str_ = "".join(str_list)
    chast_letters = {}
    for letter in str_:
        if letter.isalpha() == True:
            if letter in chast_letters:
                chast_letters[letter] += 1
            else:
                chast_letters[letter] = 1
    return chast_letters
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def persent_element (chast_letters):
    for letter in chast_letters:
        chast_letters[letter] = chast_letters[letter]/(sum(chast_letters.values())/100)
    return chast_letters
print(persent_element(get_count_char(main_str)))