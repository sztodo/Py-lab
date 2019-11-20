def progresie_aritmetica(my_list, k):
    d = 0
    for i in range(len(my_list)-2):
        if my_list[i+1] - my_list[i] == k:
           continue
        else:
            d += 1
    if d==0:
        print("Progresie aritmetica")
    else:
        print("Nu e progresie aritmetica")

my_list = []
my_list.append(eval(input('x=')))
while True:
    my_list.append(eval(input('x=')))
    if my_list[-1] == -1:
        break
k = my_list[1] - my_list[0]
progresie_aritmetica(my_list, k)
