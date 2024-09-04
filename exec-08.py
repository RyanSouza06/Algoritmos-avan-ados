#Inputs

#Qual a quantidade de votos brancos?
#nulos?
#válidos?
#============================================
#Output
#Total de porcentagens

#Total de votos válidos: x%
#Total de votos em branco: y%
#Total de votos nulos: t%

brc = int (input('Quantidade de votos brancos: '))
nulos = int (input('Quantidade de votos nulos: '))
val = int (input('Quantidade de votos válidos: '))
total = int (brc+nulos+val)
print(total)
cent_brc = int ((brc/total)*100)
cent_nulos = int ((nulos/total)*100)
cent_val = int((val/total)*100)
print("Porcentagem de votos em brancos:", cent_brc, "%")
print("Porcentagem de votos nulos:", cent_nulos, "%")
print("Porcentagem de votos totais:", cent_val, "%")
