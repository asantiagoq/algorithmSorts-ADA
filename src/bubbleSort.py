def bubbleSort(arr):
  result = arr
  n = len(result)
  for i in range(n):
    for j in range(0, n - i - 1):
      if result[j] > result[j + 1]:
        aux = result[j]
        result[j] = result[j + 1]
        result[j+1] = aux
  return result
