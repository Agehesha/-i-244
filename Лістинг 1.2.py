def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        min_index = i
        assignments += 1  # min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # обмін (3 присвоювання)

    return arr, comparisons, assignments


# Приклад використання (варіант 24)
sequence = [53, 5, 44, 47, 35, 83, 82, 85, 28]
sorted_arr, comps, assigns = selection_sort(sequence.copy())

print("Сортування вибором")
print("Відсортований масив:", sorted_arr)
print("Кількість порівнянь:", comps)
print("Кількість присвоєнь:", assigns)
