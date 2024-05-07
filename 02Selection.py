'''def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if(arr[i] > arr[j]):
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index], arr[i]

n = int(input("\nEnter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

selection_sort(arr)
print(arr)'''

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index] ,arr[i]

n = int(input("\nEnter total number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"\nEnter element {i+1}: ")))

print("\nList before sorting: ",arr)
selection_sort(arr)
print("\nList after sorting: ",arr)