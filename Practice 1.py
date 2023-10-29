# первая задача
# stroka = input("вводи: ")  
# schitat = stroka.count(' ') + 1  
# print(schitat)

# вторая задача
stariy = "В 2022 году я буду все делать вовремя!"
noviy = stariy.replace("2022", "2023")
print(noviy)

# третья задача
def srednee(grades):
    return sum(grades) / len(grades)
ocenki = input("введи оценки: ")
ocenkiSpisok = list(map(int, ocenki.split()))
average = srednee(ocenkiSpisok)
print(average)