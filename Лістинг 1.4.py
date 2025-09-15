def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1

        j = i - 1
        assignments += 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j >= 0:
            comparisons += 1

        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments


sequence = [53, 5, 44, 47, 35, 83, 82, 85, 28]
sorted_arr, comps, assigns = insertion_sort(sequence.copy())

print("Сортування вставками")
print("Відсортований масив:", sorted_arr)
print("Кількість порівнянь:", comps)
print("Кількість присвоєнь:", assigns)
