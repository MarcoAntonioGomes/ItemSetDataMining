import csv
import copy
arq = open('Vend-Prod-2008a2017-Janeiro', 'w')


path = 'venda_produto.csv'
path2 = 'produtos.csv'
vendaProd = []
listProd = []
vendaProdMat = []
ano = 2015
mes = 1

def loadCSV():
    file = open(path, newline='')
    reader = csv.reader(file,delimiter=';')

    lineNumber = 0;
    for line in reader:
       if(lineNumber == 1):
              venda = []
              venda.append(line[5])
              vendaProd.append(venda)

       aux = []
       aux.append(line[5])

       x = line[0].split("/")

       if (lineNumber > 1 and(len(x)==3)):
           mesloop = int(x[1])
           if (mesloop == '01'):
               mesloop = mes
           # print("X: ",x[1]," mes: ",mes)
           # print(mesloop == mes)
       if(((lineNumber > 1) and (aux not in vendaProd)and (int(mesloop) == int(mes)))): #and (int(x[2]) == int(ano)))):
           venda = []
           venda.append(line[5])
           vendaProd.append(venda)

       lineNumber += 1

    vendaProdMat =  copy.deepcopy(vendaProd)

    file = open(path, newline='')
    reader = csv.reader(file, delimiter=';')

    for line in reader:
         for i in range(len(vendaProd)):
            if(vendaProd[i][0] == line[5]):

                vendaProd[i].append(line[6])


    file = open(path2, newline='')
    reader = csv.reader(file, delimiter=';')

    for line in reader:
        listProd.append((line[0],line[1]))
    listProd.remove(listProd[0]);

    for i in range(len(vendaProd)):
        for  j in range(1,len(vendaProd[i])):
            for k in range(len(listProd)):
                aux = listProd[k]
               # print("Cod: ",vendaProd[i][j])
                #print("ListaCod: ",aux[0])
                if(vendaProd[i][j] == aux[0]):
                    #print("entrei aqui")
                    vendaProdMat[i].append(aux[1])


    return (vendaProdMat)





vendaProdMat = loadCSV()
print(vendaProdMat)
transactions = []
'''
for i in range(len(vendaProdMat)):
    aux = []
    for j in range(1, len(vendaProdMat[i])):
        aux.append(vendaProdMat[i][j])
    transactions.append(tuple(aux))
    #if(i == inc):
       # itemsets, rules = apriori(transactions, min_support=0.3, min_confidence=0.5)
        #print(rules)
        #inc = inc + 50
        #transactions = []

print(transactions)
'''

value = ''
for i in range(len(vendaProdMat)):
    if (len(vendaProdMat[i]) > 2):
        for j in range(1, len(vendaProdMat[i])):
            value = value + vendaProdMat[i][j].replace(" ", "_") + " "
        value = value + "\n"
        arq.write(value)
        value = ''

arq.close()
