####################
#    String Extract     #
####################

str = "X-DSPAM-Confidence: 0.8475"

index_of_colon = str.find(':')
extracted_string = str[(index_of_colon  + 1) : len(str)]
string_to_num = float(extracted_string.strip())

print "Extracted string (or floating point number) is ", string_to_num