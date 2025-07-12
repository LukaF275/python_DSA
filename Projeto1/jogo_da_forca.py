word = input("Digite uma palavra para descobrirmos:\n")

word_list = []
answer = []

print ("jogo da forca: \n")

for i in answer:
    i = " - "

for i in word:
    print("-",end = " ")

for i in word:
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
            break
    tentativas = tentativas - 1
    