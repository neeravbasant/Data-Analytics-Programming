########################
#    Score to Grade    #
########################

score = float(raw_input("Enter score: "))

# Assigning grade to respective scores

while score >= 0.0 and score <= 1.0:
  
  if score >= 0.9:
    grade = 'A'
  elif score >= 0.8:
    grade = 'B'
  elif score >= 0.7:
    grade = 'C'
  elif score >= 0.6:
    grade = 'D'
  else:
    grade = 'F'

  print "Grade is %c" % grade
  break

else:
  print "Oops! Not a valid score."