immutable_var=1,2,3,4,True,'string'
print(immutable_var)
#immutable_var[2]=10
#print(immutable_var)#кортеж не поддерживает обращение по элементам. Кортеж-это неизменяемая коллекция,
# которая может содержать в себе разные типы данных.
mutable_list=(['apple','coconut','babana'],1,2)
print(mutable_list)
mutable_list[0][2]='nut'
print(mutable_list)