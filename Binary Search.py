pos = -1

def search(list, find):
    i=0
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if(list[mid]<find):
            l=mid+1
        else:
            u=mid-1
        if(list[mid]==find):
            globals()['pos']=mid
            return True
    return False



list=[3,5,0,6,8]

list.sort()

print(list)

find=9

if search(list, find):
    print("Found at ",pos+1)
else:
    print("Not Found")