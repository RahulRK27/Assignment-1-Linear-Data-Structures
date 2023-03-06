# Write a program to find all pairs of an integer array whose sum is equal to a given number


def sum_pairs(arr , num , sum):
    for i in range(num):
        for j in range(i+1 , num):
            if arr[i] + arr[j] == sum:
                print("(",arr[i],",",arr[j],")",sep = "")
                
                
                
# drive the code
arr = [5, 6, 4, 5, 1, 9, 3, 7, 2, 8]
num = len(arr)
sum = 10


sum_pairs(arr,num,sum)