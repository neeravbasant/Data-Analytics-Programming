##############################
#     Score to Grade - Function      #
##############################

def computegrade(score):

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

    return grade
    break

  else:
    grade = "NA! Not a valid score entered."
    return grade

score = float(raw_input("Enter score: "))
print "Grade is " + computegrade(score)