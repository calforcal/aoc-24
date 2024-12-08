def read_file_into_array(txt):
  lines = []
  with open(txt, "r") as file:
      for line in file:
        stripped = line.strip()
        report = stripped.split(" ")
        lines.append(report)
      
  return lines

def validate_report(report):
  i = 0
  is_increasing = True if int(report[i]) < int(report[i + 1]) else False
  while i < len(report) - 1:
     increased = True if int(report[i]) < int(report[i + 1]) else False
     abs_value = abs(int(report[i]) - int(report[i + 1]))
     if abs_value == 0 or abs_value > 3:
        return False
     
     if increased is not is_increasing:
        return False
     i += 1
  return True

def is_increasing(report):
    decreased = 0
    increased = 0
    i = 0
    j = 1
    while i < len(report) - 1 and j < len(report):
        if int(report[i]) < int(report[j]):
           increased += 1
        else:
           decreased += 1
    
        i += 1
        j += 1
    if increased > 1 and decreased > 1:
       return None
    elif increased > 1 and decreased <= 1:
       return True
    elif increased <=1 and decreased > 1:
       return False
    else:
       return None
    
def validate_current_and_next(report, i, j):
     report_1 = report.copy()
     report_2 = report.copy()
     del report_1[i]
     del report_2[j]
     second_to_last = validate_report(report_1)
     last = validate_report(report_2)
     if second_to_last or last:
         return True
     else:
         return False


def validate_report_with_fault(report):
     i = 0
     j = 1
     is_it_increasing = is_increasing(report)

     total_faults = 0
     while i < len(report) - 1 and j < len(report):
       if j == len(report) - 1:
          return validate_current_and_next(report, i, j)
       
       increased = True if int(report[i]) < int(report[j]) else False
       abs_value = abs(int(report[i]) - int(report[j]))

       if abs_value == 0 or abs_value > 3:
           total_faults += 1
      
       if increased != is_it_increasing:
           total_faults += 1
    
       if total_faults > 0:
          return validate_current_and_next(report, i, j)
       else:
          i += 1
          j += 1
     remove_current = report
     del remove_current[i]

     return validate_report(remove_current)

def count_valid_reports(reports):
   count = 0
   for report in reports:
      count += 1 if validate_report(report) else 0

   return count

def count_valid_reports_with_faults(reports):
   count = 0
   for report in reports:
      count += 1 if validate_report_with_fault(report) else 0

   return count

def calculate_reports(txt):
   reports = read_file_into_array(txt)
   num_valid_reports = count_valid_reports(reports)
   return num_valid_reports

def calculate_reports_with_faults(txt):
   reports = read_file_into_array(txt)
   num_valid_reports = count_valid_reports_with_faults(reports)
   return num_valid_reports

def count_reports():
   return len(read_file_into_array("./data.txt"))

test_reports = calculate_reports("./example_data.txt")
print("Test Data Report Count -> ", test_reports)

reports = calculate_reports("./data.txt")
print("Report Count -> ", reports)

test_reports_with_faults = calculate_reports_with_faults("./example_data.txt")
print("Test Data Report Count -> ", test_reports_with_faults)

reports_with_faults = calculate_reports_with_faults("./data.txt")
print("Report Count -> ", reports_with_faults)