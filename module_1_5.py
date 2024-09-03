#immutable_var=1,3,5,'dog','cat','#'
#print(immutable_var)
#immutable_var[0]=7 # кортеж не поддерживает обращение по элементам. Можно изменить элементы списка,которые находятся внутри кортежа
#print(immutable_var)

mutable_list=[3,5,7,'dog','cat']
mutable_list[1]=0
mutable_list[3]='@'
print(mutable_list)