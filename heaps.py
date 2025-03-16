import heapq

A = [1, 3, 5, 7, 9 ,2, 4, 6, 8, 0]
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list

def maxheap(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = -arr[i]
    heapq.heapify(arr)
    for i in range(n):
        arr[i] = -arr[i]
    return arr

heapq.heapify(A)
print(A)
sorted_heap = heapsort(A)
print(sorted_heap)
max_heap = maxheap(B)
print(max_heap)
