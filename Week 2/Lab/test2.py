import sys
sys.path.append('C:\Users\Neerav Basant\Documents\GitHub\Data-Analytics-Programming\Week 2\Lab')

import bear_matching

computed_result = bear_matching.matching_bears("C:/Users/Neerav Basant/Documents/GitHub/Data-Analytics-Programming/Week 2/Lab/medium-1.dat")
expected_result = [("pat", "jack the great"), ("deb", "jack the great")]

computed_result.sort()
expected_result.sort()
assert computed_result == expected_result
print "Successfully passed test2!"