A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    m = n // 2
    l = arr[:m]
    r = arr[m:]

    l = merge_sort(l)
    r = merge_sort(r)
    i, lp, rp = 0, 0, 0
    l_len = len(l)
    r_len = len(r)

    sorted_arr = [0] * n

    while lp < l_len and rp < r_len:
        if l[lp] < r[rp]:
          sorted_arr[i] = l[lp]
          lp += 1
        else:
          sorted_arr[i] = r[rp]
          rp += 1
        i += 1

    while lp < l_len:
        sorted_arr[i] = l[lp]
        lp += 1
        i += 1

    while rp < r_len:
        sorted_arr[i] = r[rp]
        rp += 1
        i += 1

    return sorted_arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p = arr[-1]
    l = [x for x in arr[:-1] if x <= p]
    r = [x for x in arr[:-1] if x > p]

    l = quick_sort(l)
    r = quick_sort(r)

    return l + [p] + r

print(quick_sort(A))
