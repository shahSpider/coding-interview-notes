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


If x goes out of scope, like this:

def my_func():
    x = 10  # x is local to this function

my_func()

Now the integer 10 might be cleaned if:
    There are no other references to 10 (rare, because small ints like 10 are interned)
    Python's memory manager decides it’s time to release it

After this point, x is out of scope and deleted

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


🌀 What Is a Generator?
A generator is a special kind of iterable that yields items one at a time, only when needed — rather than storing everything in memory.

def count_up_to(n):
	count = 0
	while count < n:
		yield count
		count += 1

gen = count_up_to(5)

for num in gen:
	print(num)

Generators Expression

squares = (x * x for x in range(5))
for s in squares:
	print(s)

gen = (x * x for x in range(3))      # Generator (lazy)
lst = [x * x for x in range(3)]      # List (eager)
tpl = tuple(x * x for x in range(3)) # Tuple (eager, from generator)

Note: There’s no such thing as a "tuple comprehension" like [x for x in ...] but with () — that’s actually a generator expression.

Real-World Use Cases for Generators
    • Streaming files line-by-line
    • Processing large datasets
    • Producing infinite sequences
    • Pipeline-style data transformations

📦 What’s an Iterator?
An iterator is an object that represents a stream of data — you can loop through it one element at a time, but only in one direction.
All generators are iterators,
but not all iterators are generators.


🧠 What is GIL?

GIL = Global Interpreter Lock

    A mutex (lock) that protects access to Python objects.

    Allows only one thread to execute Python bytecode at a time, even on multi-core systems.

    Exists in CPython (most common Python implementation) for memory management safety (due to reference counting).

    💡 GIL means multi-threading in Python doesn’t give true parallelism for CPU-bound tasks.

🔁 asyncio — Asynchronous I/O (Concurrency)

    Single-threaded, single-process, but non-blocking.

    Used for I/O-bound tasks: network calls, DB access, file I/O.

    Uses async / await syntax.

✅ Example:

import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    print("Data fetched!")

asyncio.run(fetch_data())

    ⚡ Efficient for handling thousands of tasks, like web scraping or APIs.


🔄 Threads — Concurrency with GIL

    Use the threading module.

    Good for I/O-bound tasks (waiting for network, disk, etc.).

    ⚠️ Not great for CPU-bound tasks due to GIL.

✅ Example:

import threading

def greet():
    print("Hello!")

thread = threading.Thread(target=greet)
thread.start()


⚙️ Multiprocessing — Parallelism

    Uses multiple processes, not threads.

    Each process has its own Python interpreter + memory space ⇒ no GIL interference.

    Best for CPU-bound tasks (heavy computations).

✅ Example:

from multiprocessing import Process

def compute():
    print("Computing...")

p = Process(target=compute)
p.start()

    🧠 True parallelism via multiple CPU cores.



# Object Oriented Programming OOP
Absolutely! Let’s go through the **4 Pillars of Object-Oriented Programming (OOP)** using **Python**, with **detailed concepts** and **example code** for each.

---

## 🧱 1. **Encapsulation**
> Bundling data and methods into a single unit (class), and **restricting direct access** to some of the object’s components.

### ✅ Concept:
- Keep internal object details **private** or **protected**.
- Expose only what’s needed using **getters/setters**.

### 🧪 Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# account.__balance  ❌ Error: private attribute
```

---

## 🧱 2. **Abstraction**
> Hiding **complex implementation details**, and showing only the **essential features**.

### ✅ Concept:
- Use **abstract classes** or **interfaces**.
- Focus on **what** an object does, not **how**.

### 🧪 Example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Polymorphic behavior
```

---

## 🧱 3. **Inheritance**
> Allows one class (child) to **inherit** attributes and methods from another (parent).

### ✅ Concept:
- Promotes **code reuse**.
- Use `super()` to access parent class behavior.

### 🧪 Example:
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is moving...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

car = Car("Toyota", "Corolla")
car.drive()
```

---

## 🧱 4. **Polymorphism**
> The ability to **take many forms** — same interface, different implementations.

### ✅ Concept:
- Method overriding (same method, different behavior in subclass)
- Works well with **inheritance and abstraction**

### 🧪 Example:
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())  # Different output, same interface
```

---

## 🎯 Summary Table:

| Pillar         | Meaning                            | Python Example                      |
|----------------|------------------------------------|--------------------------------------|
| Encapsulation  | Data hiding                        | Private vars `__var`, getters/setters |
| Abstraction    | Hiding complexity                  | ABCs & `@abstractmethod`            |
| Inheritance    | Reuse properties/methods           | `class Child(Parent)`               |
| Polymorphism   | One interface, many behaviors      | Method overriding                   |

---

Let me know if you want a **real-world OOP project demo** (e.g., ATM, School System, etc.) using all 4 principles together!