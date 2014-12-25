#################################
#    Calculating Basic Statistics     #
#################################

# Asking user for the entry and appending them to one list

num_list = []
flag = 1
while flag == 1:
  try :
    num = raw_input("Enter Number: ")
    num = num.lower()
    if num != 'done':
      num_list.append(float(num))
    elif num == 'done':
      flag = 0
  except:
    print "Wrong Entry! Enter a number or 'done'"

# Calculating and printing basic statistics for the final list

total = sum(num_list)
count = len(num_list)
average = total/count
min = min(num_list)
max = max(num_list)

print "Sum is %f" % total
print "Count is %f" % count
print "Average is %f" % average
print "Minimum is %f" % min
print "Maximum is %f" % max