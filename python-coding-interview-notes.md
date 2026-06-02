# PYTHON INTERVIEW NOTES

## Python Code Execution
    - Both Compile (not exactly like other languages such as Java/C++) and Interpreter
    - Source code which is .py and Compiled code (bytes) is stored in .pyc
    - Compilers like Cpython, Jython,


## Python Memory Management
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


    | List        | Tuple       |
    | ----------- | ----------- |
    | Mutable     | Immutable   |
    | Slower      | Faster      |
    | More memory | Less memory |
    | []          | ()          |

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


## Python Memory Management (Core Idea)

    Python manages memory using:

    Private heap + reference counting + garbage collector

    Everything in Python is an object stored in memory, and Python decides:

    when to allocate memory
    when to free it
    1. Memory Allocation in Python

    When you do:

    x = 10

    Python:

    creates an integer object (10)
    stores it in heap memory
    x becomes a reference (pointer) to that object

    So:

    x  ───▶  [ 10 in heap memory ]
    2. Reference Counting (Main Mechanism)

    Every object has a reference count = number of variables pointing to it.

    Example:

    a = [1, 2, 3]
    b = a

    Now:

    [1,2,3] → ref count = 2

    Because:

    a points to it
    b points to it
    When reference count becomes 0
    del a
    del b

    Now:

    ref count = 0

    👉 Python immediately frees memory.

    This is called:

    Automatic memory deallocation

    3. Garbage Collector (GC)

    Reference counting alone cannot handle:

    🔴 Circular references problem
    a = []
    b = []

    a.append(b)
    b.append(a)

    Now:

    a ↔ b (cycle)

    Even if you delete both:

    del a
    del b

    They still reference each other → ref count is NOT zero

    Solution: Garbage Collector

    Python has a cyclic garbage collector:

    Detects cycles
    Frees unreachable objects
    Runs periodically



## Deep Copy vs Shallow Copy

### Shallow Copy

    Copies outer object only.

    import copy

    a = [[1,2],[3,4]]
    b = copy.copy(a)

    Inner lists are shared.

### Deep Copy
    b = copy.deepcopy(a)





## SCOPE IN PYTHON

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


## What Is a Generator?
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

    ### INTERVIEW QUESTION:

    def test():
        for i in range(1, 10):
            yield i

    g = test()

    print(list(g))
    print(list(g))

    OUTPUT:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    []
    The first list(g) consumes the generator completely, leaving nothing for the second call.

    A generator is an iterator that produces values lazily. It can be looped over with a for loop, but once consumed, it cannot be reused without creating a new generator instance.


    Real-World Use Cases for Generators
        • Streaming files line-by-line
        • Processing large datasets
        • Producing infinite sequences
        • Pipeline-style data transformations

## What’s an Iterator?
    An iterator is an object that represents a stream of data — you can loop through it one element at a time, but only in one direction.
    All generators are iterators,
    but not all iterators are generators.

    # Iterator vs Generator

    An iterator is any object that implements the iterator protocol (__iter__ and __next__). A generator is a simpler way to create an iterator using the yield keyword. Python automatically manages the iterator behavior for generators, making them more concise and memory-efficient.


    The real difference is where the values come from
    Iterator over a list
    nums = [1, 2, 3]
    it = iter(nums)

    The data already exists in memory:

    nums
    ├─ 1
    ├─ 2
    └─ 3

    The iterator is just keeping track of position:

    current index = 0

    When you call next(it), it returns the next existing element.

    Generator
    def gen():
        yield 1
        yield 2
        yield 3

    No list exists.

    No values are stored upfront.

    Instead, Python remembers:

    Function state
    Current execution point
    Local variables

    When you call:

    next(g)

    Python resumes executing the function until the next yield.

    A clearer example
    List iterator
    nums = [x * x for x in range(1000000)]
    it = iter(nums)

    First:

    create 1,000,000 values
    store them in memory

    Then:

    iterator walks through them
    Generator
    g = (x * x for x in range(1000000))

    No million values are created.

    When you do:

    next(g)

    only one value is computed.

    Then the next one.

    Then the next one.

    Another way to think about it
    Iterator
    Data already exists
            ↓
    Iterator walks over it

    Example:

    iter(list)
    iter(tuple)
    iter(dict)
    iter(set)
    Generator
    Data is produced on demand
            ↓
    Generator creates values lazily

    Example:

    def gen():
        yield ...
    Interview answer

    If asked:

    If iter(list) and a generator both support next(), what's the difference?

    Answer:

    iter(list) returns an iterator that traverses data already stored in memory. A generator is itself an iterator, but it computes or produces values lazily using yield, generating them only when requested. The interface is similar (next()), but the source of the values is different.


    Absolutely! Let’s go deeper into the **differences between `iter(list)` and a generator expression** in terms of:

    * 🔋 **Memory usage**
    * 🔁 **Reusability**

    ---

    ## 🔋 1. **Memory Usage**

    ### ✅ `iter(list)`:

    ```python
    my_list = [1, 2, 3]
    it = iter(my_list)
    ```

    * The **list already exists in memory**, so `iter()` just creates a **lightweight wrapper** around it.
    * You're **not saving memory**, you're just **consuming the same list lazily**.
    * The entire list is still stored in RAM.

    ### ✅ `(x for x in list)` (Generator expression):

    ```python
    gen = (x for x in my_list)
    ```

    * The generator **does not store values in memory**.
    * It generates each value **on-the-fly** as you loop or call `next()`.
    * This is **memory-efficient**, especially for **large datasets or infinite streams**.

    ---

    ### 💡 TL;DR:

    | Operation            | Memory Usage                                    |
    | -------------------- | ----------------------------------------------- |
    | `iter(list)`         | List is **already in memory**                   |
    | Generator expression | Values are **created on demand** — saves memory |

    ---

    ## 🔁 2. **Reusability**

    ### ✅ `iter(list)`:

    ```python
    it1 = iter(my_list)
    it2 = iter(my_list)
    ```

    * Since the original list is unchanged, you can create **new iterators again and again**.
    * You can even re-iterate over the list with a `for` loop later.

    ### ❌ Generator expression:

    ```python
    gen = (x for x in my_list)
    ```

    * A generator is a **one-time-use** object.
    * Once you **exhaust it** (by looping or calling `next()`), it’s **done forever**.

    ```python
    for i in gen:
        print(i)  # This works

    for i in gen:
        print(i)  # Nothing prints! It's already exhausted
    ```

    ---

    ### 💡 TL;DR:

    | Operation            | Reusability              |
    | -------------------- | ------------------------ |
    | `iter(list)`         | ✅ Can recreate iterators |
    | Generator expression | ❌ One-time use only      |

    ---

    ## ✅ Summary Table

    | Feature      | `iter(list)`                    | Generator Expression (`(x for x in list)`) |
    | ------------ | ------------------------------- | ------------------------------------------ |
    | Memory usage | List is already in memory       | Creates values lazily (saves memory)       |
    | Reusability  | Can call `iter()` again anytime | Once used, it's exhausted                  |
    | Use case     | When you already have the data  | When you want efficient, on-the-fly values |

    ---



## What is GIL?

    GIL = Global Interpreter Lock

        A mutex (lock) that protects access to Python objects.

        Allows only one thread to execute Python bytecode at a time, even on multi-core systems.

        Exists in CPython (most common Python implementation) for memory management safety (due to reference counting).

        💡 GIL means multi-threading in Python doesn’t give true parallelism for CPU-bound tasks.


    First: What problem does the GIL solve?

    Imagine multiple threads modifying Python objects simultaneously.

    counter = 0

    # Thread 1
    counter += 1

    # Thread 2
    counter += 1

    The statement:

    counter += 1

    is not actually one operation.

    Python roughly performs:

    LOAD counter
    ADD 1
    STORE counter

    If two threads execute these steps simultaneously:

    Thread 1: LOAD counter (0)
    Thread 2: LOAD counter (0)

    Thread 1: ADD 1 => 1
    Thread 2: ADD 1 => 1

    Thread 1: STORE 1
    Thread 2: STORE 1

    Expected:

    2

    Actual:

    1

    This is called a race condition.

    CPython's solution

    The main Python interpreter, CPython, uses a Global Interpreter Lock.

    GIL = a giant mutex(lock)

    Before executing Python bytecode:

    Thread A acquires GIL
    Thread A executes

    Thread B waits

    Later:

    Thread A releases GIL

    Thread B acquires GIL
    Thread B executes

    Therefore:

    Only one thread executes Python bytecode at any instant.
    Important distinction

    People often say:

    "Only one thread runs at a time."

    That's not completely accurate.

    More precise:

    Only one thread executes Python bytecode at a time.

    The OS may schedule many threads.

    But only one can hold the GIL and run Python instructions.

    Why does Python have GIL?

    Without GIL:

    Python's memory management becomes much harder.

    Python objects use reference counting.

    Example:

    a = [1, 2, 3]
    b = a

    Internally:

    Reference count = 2

    When references disappear:

    del a
    del b

    Reference count changes.

    If multiple threads modify reference counts simultaneously:

    Memory corruption
    Crashes
    Segmentation faults

    The GIL protects these operations.

    CPython uses the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time. For CPU-bound workloads, threads compete for the GIL and cannot fully utilize multiple CPU cores. For such tasks, multiprocessing is preferred because each process has its own interpreter and GIL.

    ANALOGY OF GIL
    Thread model (GIL world):
        One kitchen (one interpreter)
        Multiple chefs (threads)
        One stove (GIL)
    Process model:
        Multiple kitchens (multiple interpreters)
        Each kitchen has its own stove
        No sharing by default



## asyncio — Asynchronous I/O (Concurrency)

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


## Threads — Concurrency with GIL

    Use the threading module.

    Good for I/O-bound tasks (waiting for network, disk, etc.).

    ⚠️ Not great for CPU-bound tasks due to GIL.

    ✅ Example:

    import threading

    def greet():
        print("Hello!")

    thread = threading.Thread(target=greet)
    thread.start()


## Multiprocessing — Parallelism

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



## Object Oriented Programming OOP
    Absolutely! Let’s go through the **4 Pillars of Object-Oriented Programming (OOP)** using **Python**, with **detailed concepts** and **example code** for each.


#### 🧱 1. **Encapsulation**
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

## 🔷 What is MRO in Python?

**MRO = Method Resolution Order**

It defines:

> The order in which Python looks for a method in a class hierarchy when multiple inheritance is involved.

In simple words:

> If a method exists in multiple parent classes, MRO decides which one is called first.

---

# 1. Simple inheritance (no confusion)

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

b = B()
b.show()
```

### Output:

```
A
```

### Why?

Python looks in this order:

```text
B → A → object
```

This is MRO.

---

# 2. Multiple inheritance (where MRO matters)

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
```

---

## ❓ Which show() will run?

Answer: **B**

---

# 3. How Python decides (MRO order)

Check it:

```python
print(D.mro())
```

Output:

```text
[D, B, C, A, object]
```

So lookup happens like:

```text
D → B → C → A → object
```

First match wins → `B.show()`

---

# 4. Key rule: C3 Linearization (important interview concept)

Python uses **C3 Linearization algorithm** to build MRO.

Rules:

1. Child class comes first
2. Left-to-right order in inheritance matters
3. No class appears twice
4. Parents are resolved after children

---

# 5. Visual understanding

```text
      A
     / \
    B   C
     \ /
      D
```

Inheritance:

```python
class B(A): pass
class C(A): pass
class D(B, C): pass
```

MRO:

```text
D → B → C → A → object
```

---

# 6. Why MRO exists (very important)

Without MRO:

```text
Ambiguity problem ❌
```

Example:

* B has `show()`
* C has `show()`

Python needs a rule to decide.

So MRO ensures:

> deterministic + predictable method lookup

---

# 7. super() and MRO (VERY IMPORTANT)

## Example:

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()
```

---

## Call:

```python
d = D()
d.show()
```

---

## Output:

```
D
B
C
A
```

---

## Why?

Because `super()` follows **MRO order**, not just parent class.

MRO is:

```text
D → B → C → A → object
```

So execution flows accordingly.

---

# 8. MRO check tools

```python
print(D.mro())
```

or

```python
print(D.__mro__)
```

---

# 9. Interview-ready definition

> MRO (Method Resolution Order) defines the order in which Python searches for methods in a class hierarchy. It is especially important in multiple inheritance and is implemented using the C3 linearization algorithm. Python follows the MRO list from child to parent, left to right, ensuring deterministic method resolution.

---

# 10. Real-world analogy

Think of:

```text
D = manager
B, C = team leads
A = worker policies
```

If manager asks for “report()”:

Python decides:

```text
Ask B first → if not found → C → then A
```

That is MRO.

---

# 🔥 Key interview points to remember

* MRO is method lookup order
* Python uses C3 linearization
* In multiple inheritance, left-most parent has priority
* `super()` follows MRO, not direct parent
* Use `ClassName.mro()` to inspect

---

If you want next level, I can explain:

* 🔥 Diamond problem in depth (very important)
* 🔥 super() internals (why it feels “magical”)
* 🔥 real Django/Frappe MRO usage in models

Just say 👍



1. Method Overriding (VERY IMPORTANT in Python)
Meaning

Method overriding happens when a child class redefines a method that already exists in the parent class.

It is runtime polymorphism.

Example
class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
Usage
a = Animal()
d = Dog()

print(a.sound())  # Some generic sound
print(d.sound())  # Bark
Key idea

Same method name → different behavior depending on object

Real backend / Frappe analogy

In Frappe Framework:

class Document:
    def validate(self):
        pass
class SalesInvoice(Document):
    def validate(self):
        self.calculate_total()

👉 Frappe overrides validate() in every DocType.

Why overriding is powerful
Custom behavior per class
Framework extensibility
Core method stays same, logic changes
2. Method Overloading (IMPORTANT: Python handles it differently)
Meaning (theoretical OOP concept)

Method overloading means having multiple methods with the same name but different parameters.

Example in Java/C++
void add(int a, int b)
void add(int a, int b, int c)

Same method name, different signatures.

BUT in Python ❗

Python does NOT support true method overloading.

If you define multiple methods with the same name:

class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

👉 The second one overwrites the first.

So what happens?
t = Test()
t.add(1, 2)

❌ Error:

TypeError: add() missing 1 required positional argument
3. How Python SIMULATES Overloading

We use default arguments or *args.

Option 1: Default arguments
class Test:
    def add(self, a, b, c=0):
        return a + b + c
t = Test()

print(t.add(2, 3))      # 5
print(t.add(2, 3, 4))   # 9
Option 2: *args (most flexible)
class Test:
    def add(self, *args):
        return sum(args)
t = Test()

print(t.add(1, 2))
print(t.add(1, 2, 3, 4))
4. Key Differences (Interview Table)
Feature	Overriding	Overloading
Definition	Redefining parent method in child	Same method name, different parameters
Where	Parent → Child classes	Same class
Python support	Yes (native)	No (simulated)
Polymorphism type	Runtime polymorphism	Compile-time polymorphism (not in Python)
Key mechanism	Inheritance	Argument variation