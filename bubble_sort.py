def bubble_sort(list1):
    for i in range(0,len(list1)-1):#0,5
        for j in range(0,len(list1)-1):#0,5
            if list1[j]>list1[j+1]:#list1[0]>list[1] i.e 5>3 returns true 
                temp = list1[j]#temp = 5 
                list1[j]=list1[j+1]#list1[j] = 3 
                list1[j+1] = temp #list1[j+1] = 5 
    return list1 
list1 = [5,3,8,6,7,3]
m = bubble_sort(list1)


print(m)
