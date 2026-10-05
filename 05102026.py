Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import builtins
dir (builins)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dir (builins)
NameError: name 'builins' is not defined. Did you mean: 'builtins'?
dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
divmod(20,4)
(5, 0)
divmod(20/5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    divmod(20/5)
TypeError: divmod expected 2 arguments, got 1
20/5
4.0
20%5
0
20//5
4
abs(-4)
4
bool(1)
True
bool(0)
False
bool(-4)
True
'10'+'10'
'1010'

name='menaga'
for i in enumerate(name):
    print(i)

    
(0, 'm')
(1, 'e')
(2, 'n')
(3, 'a')
(4, 'g')
(5, 'a')
for i in range(len(name)):
    print(i)

    
0
1
2
3
4
5
for i in range(len(name)):
    print(i,name)

    
0 menaga
1 menaga
2 menaga
3 menaga
4 menaga
5 menaga
len(name)
6

#RIGHT ANGLE TRIANGLE
for i in range(len(name)):
    for j in range(0,i):
    print(i,end=' ')
    
SyntaxError: expected an indented block after 'for' statement on line 3
for i in range(len(name)):
    for j in range(0,i):
        print(name, end=' ')
    print()

    

menaga 
menaga menaga 
menaga menaga menaga 
menaga menaga menaga menaga 
menaga menaga menaga menaga menaga 
for i in range(len(name)):
    for j in range(0,i+1):
        print(name, end=' ')
    print(i)

    
menaga 0
menaga menaga 1
menaga menaga menaga 2
menaga menaga menaga menaga 3
menaga menaga menaga menaga menaga 4
menaga menaga menaga menaga menaga menaga 5
for i in range(len(name)):
    for j in range(0,i+1):
        print([j], end=' ')
    print(i)

    
[0] 0
[0] [1] 1
[0] [1] [2] 2
[0] [1] [2] [3] 3
[0] [1] [2] [3] [4] 4
[0] [1] [2] [3] [4] [5] 5
for i in range(1,7):
    print(name[:i])

    
m
me
men
mena
menag
menaga
pov9*2
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    pov9*2
NameError: name 'pov9' is not defined
pov(9*2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    pov(9*2)
NameError: name 'pov' is not defined. Did you mean: 'pow'?
pow(9*2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    pow(9*2)
TypeError: pow() missing required argument 'exp' (pos 2)
pow(9,2)
81
for i in reversed(name):
    print(i)

    
a
g
a
n
e
m

#MAT FUNCTIONS
import math
math.comb(5,4)
5
import math
math.factorial(5)
SyntaxError: multiple statements found while compiling a single statement
import math
math.factorial(5)
120
math.gcd(5,8)
1
math.lcm(5,8)
40
#Lambda fn
def age():
    if a>b or a>c:
        print("A is greater")
    elif b>c:
        print("B is greater")
    else:
        print("C is greater")

        
a=52
b=58
c=47
def age():
    if a>b or a>c:
        print("A is greater")
    elif b>c:
        print("B is greater")
    else:
        print("C is greater")

        

>>> age()
A is greater
>>> def age():
...     if a>b:
...         print("A is greater")
...     elif b>c:
...         print("B is greater")
...     else:
...         print("C is greater")
... 
...         
>>> age()
B is greater
>>> Highest_age=lambda a,b,c:a if a>b and a>c else b if b>c else c
>>> Highest_age(40,30,10)
40
>>> 
>>> num=[1,2,3,4,5]
>>> squares=[]
>>> for in in num:
...     
SyntaxError: invalid syntax
>>> for i in num:
...     squares.append(i*i)
... print(squares)
SyntaxError: invalid syntax
>>> 
>>> for i in num:
...     squares.append(i*i)
...     
... print(squares)
SyntaxError: invalid syntax
>>> num=[1,2,3,4,5]
>>> squares=[]
>>> for i in num:
...     squares.append(i * i)
... 
...     
>>> print(squares)
[1, 4, 9, 16, 25]

#EXERCISE
def square(x):
    return x*x

print(square(2))
4

square=lanbda x:x*x
SyntaxError: invalid syntax
square=lanbda x : x * x
SyntaxError: invalid syntax
square=lambda x : x * x
print(square(6))
36
add=lambda a,b:a+b
print(add(5,20))
25
result=list(filter(lambda x:x%2==0,num))
print(result)
[2, 4]
result=reduce(lambda a,b:a+b,numbers)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    result=reduce(lambda a,b:a+b,numbers)
NameError: name 'reduce' is not defined
from functools import reduce
result=reduce(lambda a,b:a+b,numb)
print(result)
SyntaxError: multiple statements found while compiling a single statement
result=reduce(lambda a,b:a+b,num)
print(result)

15

#Math Functions
#useful in mathematical functions
import math
math.sqrt(25)
5.0
math.pow(25)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    math.pow(25)
TypeError: pow expected 2 arguments, got 1
math.pow(25,5)
9765625.0
math.ceil(5)
5
math.ceil(4.4)
5
math.floor(4.8)
4
math.factorial(5)
120
math.comb(5, 2)
10
math.gcd(12, 8)
4
math.fabs(-5)
5.0
