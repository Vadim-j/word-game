import os
import random
def update_result():
    for r in range(len(word)):
        if letter_input == word[r]:
            result[r] = letter_input
    os.system("cls")
def reader_file():
    with open("words/words.txt", "r", encoding="utf-8")as n:
        text=n.readlines()
    return text
# 1. компьютер выбирает слово
# 2. человек угадывает буквы
# 3. компьютер записывает угаданные буквы
# 
# . наоборот
used_letters = []
word_list = reader_file()
word = random.choice(word_list)[:-1]
tries = len(word)+5
result = ["-"]*len(word)
for j in range(tries):
    print(f'попытка{tries}/{len(word)+5}')
    print(result)
    print(f'{used_letters} использованные буквы')
    letter_input = input("пожалуйста назовите букву:").lower()
    if letter_input in word:
        print("угадали")
        used_letters.append(letter_input)

    else:
        print("не угадали") 
        used_letters.append(letter_input)
    tries-=1
    update_result()

    if tries < 1 or "-" not in result:
        print("конец игры")
        if "-" not in result:
            print("вы выиграли!".upper())
        else :
            print("вы проиграли!".upper())
            print(f"секретное-{word}")
        break
        