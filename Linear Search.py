pos = -1 #making global variable

def search(list, find):
    i=0

    while i<len(list):
        if list[i]==find:
            globals()['pos']=i
            return True
        i+=1
    return False

#in place of while loop for loop can also be used

list=[3,5,3,6,8]

find=5

if search(list, find):
    print("Found at ",pos+1)
else:
    print("Not Found")
