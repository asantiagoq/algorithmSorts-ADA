def insertionSort(arr):
  result = arr
  for i in range(1, len(result)):
    key = result[i]
    j = i - 1

    while j >= 0 and key < result[j]:
      result[j + 1] = result[j]
      j -= 1

    result[j + 1] = key
  return result
