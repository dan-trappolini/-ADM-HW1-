regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"'[0][0]|[1][1]|[0]\d[0]|[1]\d[1]|[2]\d[2]|[3]\d[3]|[4]\d[4]|[5]\d[5]|[6]\d[6]|[7]\d[7]|[8]\d[8]|[9]\d[9]'"	




import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
