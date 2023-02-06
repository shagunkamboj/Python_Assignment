l = ["a","b","c","d","e"]
a = input("enter the value that you want to search")
for i in range(0,len(l)):
    if a == l[i]:
        print("element found at =",i)
        break
else:
    print("element not found")