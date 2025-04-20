#imprimindo tudo e uma unica linha
arquivo = open("salarios.csv","r")
data = arquivo.read()
print(data.split())

#dividindo em linhas colunas

arquivo = open("salarios.csv","r")
data = arquivo.read()
rows = data.split("\n")#divide por quebra de linhas

full_data = []



for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)

# contando linhas
cont = 0
for row in full_data:
    cont += 1

print(cont)
print("\n")

#contando colunas 
cont = 0
for i in full_data[0]:
    cont +=1
print(cont)
