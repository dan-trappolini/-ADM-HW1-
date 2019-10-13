M='M{0,3}'
C='(C[MD]|D?C{0,3})'
X='(X[MDCL]|L?X{0,3})'
I='(I[MDLVX]|V?I{0,3})'
regex_pattern = M+C+X+I+'$'
import re
print(str(bool(re.match(regex_pattern, input()))))
