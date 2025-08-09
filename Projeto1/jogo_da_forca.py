import random 


answer_list = ['banana','maca','abacate']
answer_choice = random.choice(answer_list)

print(answer_choice)

word_list = []
answer = []

print ("jogo da forca: \n")

for i in answer:
    i = " - "

for i in answer_choice:
    print("-",end = " ")

for i in answer_choice:
    word_list.append(i)

tentativas = 10
while (tentativas > 0):
    letter = input("Digite uma letra aí: ")
    for i in word_list:
        if (letter == i):
            answer.insert(word_list.index(i),i)
    for i in answer:
        print(i, end = " ")
        if (answer == word_list):
            tentativas = 0
            print("Congradulations!")
    tentativas = tentativas - 1

    