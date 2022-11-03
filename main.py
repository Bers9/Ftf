a=int(input("Введите число: ")) 

counter=0
summ=0
counter_zeros=0
while a!=0:
    d=a%10
    a//=10

    counter +=1
    summ+=d

    if d==0:
        counter_zeros +=1

print("Сумма", summ)
print("Кол-во цифр: ", counter)
print("Ср.ариф.: ", summ/counter)
print("Количество нулей", counter_zeros)
