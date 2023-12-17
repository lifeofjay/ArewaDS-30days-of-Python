#SyntaxError
print 'hello world'
#output: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#fixed
print('hello world')
#output: hello world

#NameError
print (age)
#output: NameError: name 'age' is not defined
#fixed 
age=25
print(age)
#output: 25
#Index error
numbers = [1, 2, 3, 4, 5]
numbers[5]
#output: IndexError: list index out of range
#fixed
numbers = [1, 2, 3, 4, 5]
numbers[3]
#output:
4
 #ModuleNotFoundError
 import maths
 #output: ModuleNotFoundError: No module named 'maths'
 #fixed
 import math
 #AttributeError
 import math
math.PI
#output : AttributeError: module 'math' has no attribute 'PI'
#fixed
import math
math.pi
#output: 3.141592653589793
#Keyerror
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['name']
#output:'Asab'
users['county']
#Output: KeyError: 'county'
#fixed
users['country']
# output:
'Finland'

TypeError
4 + '3'
#output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
#fixed
4+int('3')
4+float('3')
#output: 7
#output: 7.0

#ImportError
from math import power
#output: ImportError: cannot import name 'power' from 'math' (unknown location)
#fixed 
from math import pow
pow(2,3)
#Output: 8.0

#ValueError
int('12a')
#output: ValueError: invalid literal for int() with base 10: '12a'
#Fixed
int('12')
#output: 12

#ZeroDivisionError
1/0
#output: ZeroDivisionError: division by zero


