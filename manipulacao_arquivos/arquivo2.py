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

#contando colunas 

cont = 0 

#solucionar problema do nome: nome e sobrenoe sao separados por virgula, oq ue contaria uma coluna a mais. Pensar na solução