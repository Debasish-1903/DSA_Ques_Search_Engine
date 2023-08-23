import re

arr =[]

with open("lc_pb_links_ucf.txt","r") as file:
    for line in file :
        arr.append(line)


def remove_ele_with_pattern(array,pattern):

    new_arr=[]
    for ele in array :
        if pattern not in ele:
            new_arr.append(ele)

        else:
            print("Removed:"+ele) 
    return new_arr


arr=remove_ele_with_pattern(arr,"/solution")
print(len(arr))
arr=list(set(arr))


with open("lc_pb_links_clean.txt","a") as f:
    for j in arr:
     f.write(j)

