#def is_prime(n):
 #   if n <= 1:
  #      return False
  #  for i in range(2, int(n ** 0.5) + 1):
  #      if n % i == 0:
   #         return False
    #return True


#num = int(input("Ведите число: "))
#if is_prime(num):
  #  print("Число является простым.")
#else:
  #  print("Число не является простым.")


  #  def bubble_sort(arr):
       # n = len(arr)
  #      for i in range(n - 1):
 #           for j in range(0, n - i - 1):
   #             if arr[j] > arr[j + 1]:
 #                   arr[j], arr[j + 1] = arr[j + 1], arr[j]
  #      return arr


  #  array = [64, 45, 69, 26, 56, 12, 98]
  #  sorted_array = bubble_sort(array)
  #  print(sorted_array)


  #  def find_max(arr):
     #  max_element = arr[0]

     #   for num in arr:
     #       if num > max_element:
     #           max_element = num

      #  return max_element


 #   array = [6, 2, 5, 8, 7, 3]
  #  max_num = find_max(array)
 #   print("Наибольший элемент масива:", max_num)


    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b


    n = int(input("Введите номер числа Фибоначи: "))

    result = fibonacci(n)
    print(f"Число Фибоначи с номером {n} равно {result}.")


    def find_most_frequent_string(array):
        if len(array) == 0:
            return None

        counts = {}
        max_count = 0
        most_frequent_string = None

        for string in array:
            if string not in counts:
                counts[string] = 1
            else:
                counts[string] += 1

            if counts[string] > max_count:
                max_count = counts[string]
                most_frequent_string = string

        return most_frequent_string


    strings = ["59", "48", "28", "91"]
    result = find_most_frequent_string(strings)
    print(result)