def read_file_into_array(txt):
    arr = [[], []]
    with open(txt, "r") as file:
      for line in file:
        short_long = line.split("   ")
        arr[0].append(int(short_long[0]))
        arr[1].append(int(short_long[1].strip()))
    return arr

def total_distance(txt):
    arr = read_file_into_array(txt)
    arr[0].sort()
    arr[1].sort()

    total_distance = 0

    for idx, i in enumerate(arr[0]):
       distance = abs(arr[0][idx] - arr[1][idx])
       total_distance += distance
    return total_distance

def right_list_map(arr):
   dict = {}
   for num in arr:
      if num in dict:
         dict[num] += 1
      else:
         dict[num] = 1
   return dict

def similar_numbers(txt):
   arr = read_file_into_array(txt)
   total = 0
   right_map = right_list_map(arr[1])
   for num in arr[0]:
      if num in right_map:
         total += num * right_map[num]
      continue
   return total

test = total_distance("./assets/test_list.txt")
print("distance test", test)

real = total_distance("./assets/list.txt")
print("distance real", real)

test = similar_numbers("./assets/test_list.txt")
print("similar nums test", test)

real = similar_numbers("./assets/list.txt")
print("similar nums real", real)