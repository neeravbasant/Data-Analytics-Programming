import sys
sys.path.append('C:\Users\Neerav Basant\Documents\GitHub\Data-Analytics-Programming\Week 2\Lab')

import bear_matching

computed_result = bear_matching.matching_bears("C:/Users/Neerav Basant/Documents/GitHub/Data-Analytics-Programming/Week 2/Lab/medium-2.dat")
expected_result = [("child2", "child1")]

computed_result.sort()
expected_result.sort()
assert computed_result == expected_result
print "Successfully passed test3!"