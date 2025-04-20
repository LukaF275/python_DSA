#abrindo arquivo para somente leitura 

arquivo = open('arq1.txt', 'r')
print(type(arquivo)) #<class '_io.TextIOWrapper'>

#lendo o arquivo inteiro
print(arquivo.read())

#Conta o numero de caracteres do arquivo
print(arquivo.tell())

#retorna o cursor para o inicio do arquivo
arquivo = open('arq2.txt', 'w')

#escreve no arquivo
arquivo.write('Cruz de Malta\n')

arquivo.close()


arquivo = open("arq2.txt","a")

arquivo.write(" no escudo")

arquivo.close()

arquivo = open("arq2.txt","r")

print(arquivo.read())