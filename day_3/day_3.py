import re

def read_file_into_array(txt):
  lines = []
  with open(txt, "r") as file:
      for line in file:
        memory = line.strip()
        lines.append(memory)
      
  return lines

def get_multipliers(memory) -> list[tuple]:
   multipliers = re.findall(r"mul\(\d+,\d+\)", memory)
   get_nums = [re.findall(r"mul\((\d+),(\d+)\)", mul) for mul in multipliers]

   return get_nums

def get_multipliers_with_commands(memory) -> list[tuple]:
   patterns = [r"do\(\)", r"don't\(\)", r"mul\(\d+,\d+\)"]
   combined_pattern = r"|".join(patterns)
   multipliers_with_commands = re.findall(combined_pattern, memory)
   return multipliers_with_commands

def get_list_of_products(nums) -> list[int]:
   products = []
   for couple in nums:
      products.append([int(x) * int(z) for x, z in couple])
   return [product for sublist in products for product in sublist ]

def remove_donts(multipliers, incl):
   include = incl
   keep = []
   for mul in multipliers:
      if mul == "do()":
         include = True
      elif mul == "don't()":
         include = False
      else:
         if include:
            match = re.search(r"mul\((\d+),(\d+)\)", mul)
            digits = (int(match.group(1)), int(match.group(2)))
            keep.append([digits])
         else:
            continue
   return keep, include

def sum_products(products):
   return sum(products)

def compile_multipliers(data):
   sums = []
   for line in data:
    multipliers = get_multipliers(line)
    products = get_list_of_products(multipliers)
    sums.append(sum_products(products))
    
   return sum(sums)

def compile_multipliers_with_commands(data):
   sums = []
   include = True
   for line in data:
      multipliers = get_multipliers_with_commands(line)
      multipliers_left, incl = remove_donts(multipliers, include)
      products = get_list_of_products(multipliers_left)
      sums.append(sum_products(products))
      include = incl
   
   return sum(sums)

test_array = read_file_into_array("./example_data.txt")
real_array = read_file_into_array("./data.txt")


test_sum = compile_multipliers(test_array)
print("TEST SUM", test_sum)

real_sum = compile_multipliers(real_array)
print("REAL SUM", real_sum)

commands_test = compile_multipliers_with_commands(test_array)
print("commmands test: ", commands_test)

commands_sum = compile_multipliers_with_commands(real_array)
print("test 2: ", commands_sum)