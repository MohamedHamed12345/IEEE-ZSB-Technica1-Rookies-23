def insertionSort():
    arr =list(map(int, input().split()))
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    print(arr) 
 
insertionSort()


'''
Insertion Sort Algorithm 
To sort an array of size N in ascending order: 
Iterate from arr[1] to arr[N] over the array. 
Compare the current element (key) to its predecessor. 
If the key element is smaller than its predecessor, 
compare it to the elements before. Move the greater elements one
 position up to make space for the swapped element.


A sorting algorithm is said to be stable if two objects with equal keys appear 
in the same order in sorted output as they appear in the input data set

insertion sort is a stable sorting algorithm


Time Complexity: O(N2) 
Auxiliary Space: O(1)

'''
