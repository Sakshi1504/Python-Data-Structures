def bubblesort(list):
    n=len(list)
    j=1
    for i in range(n-1):
        for j in range(n-i-1):
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
        print(list)
    return list



list = [9, 3, 2, 4,5,1,8]

bubblesort(list)

print(list)