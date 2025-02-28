Python Code Execution
- Both Compile (not exactly like other languages such as Java/C++) and Interpreter
- Source code which is .py and Compiled code (bytes) is stored in .pyc
- Compilers like Cpython, Jython,


Python Memory Management
- Memory is allocated to the value forexample
	a = 10
	b = 10
	print(id(a), id(b))
	output : 134881502822928 134881502822928
	in this case both a and b will refer to the same memory location
	
	x = 'I am X'
	y = x
	print(id(x), id(y))
	output: 132582804300720 132582804300720
	in this case too both x and y refer to the same memory location
	
	x = 'I am X'
	y = x + 'and Y'

	print(id(x), id(y))
	output: 138709230937072 138709230983856
	in this case y will get a new memory location as value is changed for y

The behavior you're seeing relates to how Python handles mutable and immutable objects in memory. Let’s break down both cases:

Case 1: Dictionaries (fruits and food) - Mutable Objects
Code:
fruits = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry'
}

food = fruits           # Both 'food' and 'fruits' refer to the same dictionary object
food['p'] = 'potato'    # Modifies the dictionary in place

print(id(food), id(fruits))  # Same memory ID for both
What’s Happening?
    • Dictionaries are mutable objects in Python. 
    • When you do food = fruits, no new object is created. Instead, food becomes another reference to the same dictionary in memory. 
    • Modifying food (e.g., food['p'] = 'potato') modifies the original object because both variables point to the same memory location. 
✅ Key Point:
For mutable objects, assignment copies the reference, not the object itself.
🔗 Both fruits and food share the same memory address.

Case 2: Strings (x and y) - Immutable Objects
Code:
x = 'I am X'
y = x

print(id(x), id(y))  # Same memory ID initially
What’s Happening?
    • Strings are immutable in Python. Once created, they cannot be changed. 
    • When you do y = x, both x and y point to the same string object in memory (because it’s efficient to reuse immutable objects). 
    • If you change y, it would create a new string object instead of modifying the original one. 
✅ Example of Changing y:
y = y + ' updated'  # Creates a new string object because strings are immutable

print(id(x), id(y))  # Different memory IDs now
⚡ Key Point:
For immutable objects, any modification creates a new object in memory.
✨ x and y will have different memory addresses after reassignment.

🔍 Why This Difference?
Object Type
Mutable?
Same Memory on Assignment?
Memory Changes on Modification?
dict
✅ Yes
✅ Yes (reference copied)
❌ No (changes in place)
list
✅ Yes
✅ Yes
❌ No
str
❌ No
✅ Yes (until reassigned)
✅ Yes (creates new object)
int
❌ No
✅ Yes (until reassigned)
✅ Yes (creates new object)

🎯 Summary
    • Mutable objects (like dict, list): 
        ◦ Changes affect all references to that object. 
        ◦ Memory address remains the same after modification. 
    • Immutable objects (like str, int, tuple): 
        ◦ Any "modification" creates a new object. 
        ◦ Memory address changes after reassignment. 

Would you like examples using lists or integers for more clarity? 🚀✨


- Memory allocation (values) are stored in HEAP MEMORY
- All the code sequence is executed in STACK MEMORY
- state of variables is maintained at STACK MEMORY
- Such values which are not referenced to any variable in STACK MEMORY are called DEAD OBJECTS
- The moment Python Interpreter finds DEAD OBJECTS exists in the HEAP MEMORY immediately it will invoke the GARBAGE COLLECTOR and the garbage collector will them remove dead objects from the Heap Memory, this kind of Garbage Collector algorithm is called REFERENCE COUNTING. The Python Interpreter always keeps a table where accounts the number of references	to each object in the Heap Memory. The moment any object in the Heap Memory accounts to 0, the python interpreter declares it as the dead object and the garbage collector is invoked to clear it off.
- Reference counting algorithm
	- optimum memory utilization
	- slower speed of execution as the garbage collector is invoked frequently.
- Python is a Dynamically Typed Language whereas Java and C++ like languages are Statically Typed Language.
- In Python, "reference" means a name (or variable) that points to an object in memory. When you assign a variable to an object, you're creating a reference to that object, not copying it.

References: 
https://youtu.be/-HLk_VY5Ovc?si=F2tHCrpvysJaRn_m

SCOPE IN PYTHON

- LEGB (Local, Enclosing, Global, Built-in)
- A global variable is defined outside any function and is accessible throughout the file after its
- local variable has the scope inside the function
- to make a variable global use keyword global

# example 1 variable is declared globally
x = 'global x'

def test():
	y = 'local y'
	global x
	x = 'global x in test'
	print(x)

test()
print(x)

output:
global x in test
global x in test

# example 2 variable is not declared globally but make it global in function by keyword global

def test():
	y = 'local y'
	global x
	x = 'global x in test'
	print(x)

test()
print(x)

output:
global x in test
global x in test


Enclosing Variable and nonlocal Keyword
    • The nonlocal keyword is used in nested functions to modify a variable in the enclosing (outer) function’s scope.
    • Without nonlocal, the variable in the outer scope cannot be modified from the inner function.
# example for enclosing scope
def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
output:
inner x
outer x

# example 2 for enclosing scope

def outer():
	x = 'outer x'

	def inner():
		# x = 'inner x'
		print(x)

	inner()
	print(x)

outer()

output:
outer x
outer x

# example 3 for enclosing with nonlocal keyword to update outer nonlocal variable

def outer():
	x = 'outer x'

	def inner():
		nonlocal x
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()

output:
inner x
inner x

# all in one example
x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
print(x)

output
inner x
outer x
global x
