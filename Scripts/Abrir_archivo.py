
# file = open('./pandas/atleta.csv','r')
# print(file.read())

file = open('./pandas/atleta.csv','r')
# print(file.readlines())
# print("dos linea: \n",file.readline())  #Una linea

for i in file:
    print(i)

