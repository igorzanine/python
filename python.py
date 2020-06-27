# 1. Modulas
# 2. Floor division
# 3. Floor Approximation
# 4. String
# 5. List
# 6. Tuples
# 7. Set
# 8. Dictionaries
# 9. Compound Data Structures
# 10. Break, Continue
# 11. Zip
# 12. Enumerate
# 13. List Comprehensions
# 14. Functions, Lamba, Mop, Filter
# 15. Iterators and Generators
# 16. Errors and Exceptions / Try Statement
# 17. Reading and Writing files
# 18. Importing Local Scripts and if __name__ == '__main__': concept
# 19. Favourate Modules
# 20. Techniques for Importing Modules
# 21. Third-Party Libraries



# # % - 1. modulus (the remainder after dividing)
# r = 5%3
# print(r)
# r = 10%5
# print(r)

# # // - 2. floor division
# f = float(5/2)
# print(f)
# f = float(5//2)
# print(f)

# # 3. float approximation
# print(.1 + .1 + .1 == .3)

# # ** - exponent (a quantity representing the power to which a given number or expression is to be raised)
# e = 2**3
# print(e)
# e = 2*2*2
# print(e)

# divide by 0
# print(5/0)

# # 4. string
# s = 'Hello'
# print(s[0])
# print(len(s))
# print(s.islower())
# print(s.lower())
# print(s.count('l'))
# print(s.find('e'))
# print('{} dear {}!'.format(s, 'friend'))
# print('e' in s)
# print('l' not in s)

# # 5. list
# l = [1, 3.4, 'a string', True]
# print(l[0])
# print(l[-1])
# print(l[1:2])
# print(l[1:3])
# print(l[:3])
# print(l[1:])
# print(True in l)
# print('Hello' not in l)
# print(len(l))
# l = [3, 2, 1]
# print(max(l))
# print(min(l))
# print(sorted(l))
# l = ['John', 'Peter', 'Sam']
# print(', '.join(l))
# l.append('Bob')
# print(l)

# # 6. tuples - immutable ordered sequences of elements
# t = (10, 5, 20)
# print(t)
# t = 15, 7, 30
# print(t)
# l, w, h = t
# print('{} x {} x {}'.format(l, w, h))
# t = l, w, h
# print(t)

# # 7. set - mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.
# numbers = [1, 2, 6, 3, 1, 1, 6]
# unique_nums = set(numbers)
# print(unique_nums)
# fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
# print("watermelon" in fruit)  # check for element
# fruit.add("watermelon")  # add an elementprint(fruit)
# print(fruit.pop())  # remove a random element
# print(fruit)

# # 8. dictionaries - A dictionary is a mutable data type that stores mappings of unique keys to values.
# elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
# print(elements["helium"])  # print the value mapped to "helium"
# elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
# print("carbon" in elements)
# print(elements.get("dilithium"))
# n = elements.get("dilithium")
# print(n is None)
# print(n is not None)

# # 9. Compound Data Structures - include containers in other containers to create compound data structures.
# elements = {"hydrogen": {"number": 1,
#                          "weight": 1.00794,
#                          "symbol": "H"},
#               "helium": {"number": 2,
#                          "weight": 4.002602,
#                          "symbol": "He"}}
#
# helium = elements["helium"]  # get the helium dictionary
# hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
# print(helium)
# print(hydrogen_weight)
# oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
# elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
# print('elements = ', elements)

# Mutability is about whether or not we can change an object once it has been created.
# Order is about whether the position of an element in the object can be used to access the element.
# Both strings and lists are ordered.

# 10. break, continue
# manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
#
# # the code breaks the loop when weight exceeds or reaches the limit
# print("METHOD 1")
# weight = 0
# items = []
# for cargo_name, cargo_weight in manifest:
#     print("current weight: {}".format(weight))
#     if weight >= 100:
#         print("  breaking loop now!")
#         break
#     else:
#         print("  adding {} ({})".format(cargo_name, cargo_weight))
#         items.append(cargo_name)
#         weight += cargo_weight
#
# print("\nFinal Weight: {}".format(weight))
# print("Final Items: {}".format(items))
#
# # skips an iteration when adding an item would exceed the limit
# # breaks the loop if weight is exactly the value of the limit
# print("\nMETHOD 2")
# weight = 0
# items = []
# for cargo_name, cargo_weight in manifest:
#     print("current weight: {}".format(weight))
#     if weight >= 100:
#         print("  breaking from the loop now!")
#         break
#     elif weight + cargo_weight > 100:
#         print("  skipping {} ({})".format(cargo_name, cargo_weight))
#         continue
#     else:
#         print("  adding {} ({})".format(cargo_name, cargo_weight))
#         items.append(cargo_name)
#         weight += cargo_weight
#
# print("\nFinal Weight: {}".format(weight))
# print("Final Items: {}".format(items))

# # 11. zip
# letters = ['a', 'b', 'c']
# nums = [1, 2, 3]
# for letter, num in zip(letters, nums):
#     print("{}: {}".format(letter, num))
# some_list = [('a', 1), ('b', 2), ('c', 3)]
# letters, nums = zip(*some_list)
# print('{} : {}'.format(letters, nums))

# # 12. enumerate
# letters = ['a', 'b', 'c', 'd', 'e']
# for i, letter in enumerate(letters):
#     print(i, letter)
# cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
# cast_heights = [72, 68, 72, 66, 76]
# cast = dict(zip(cast_names, cast_heights))
# print(cast)
# cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# names, heights = zip(*cast)
# print(names)
# print(heights)
# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# data_transpose = tuple(zip(*data))
# print(data_transpose)
# cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
# heights = [72, 68, 72, 66, 76]
# for i, name in enumerate(cast):
#     cast[i] = '{} {}'.format(name, heights[i])
# print(cast)

# # 13. list comprehensions
# cities = ['new your', 'seattle', 'boston']
# cap_cities = [city.title() for city in cities]
# print(cap_cities)
# squares = [x**2 for x in range(9)]
# print(squares)
# squares = [x**2 for x in range(9) if x % 2 == 0]
# print(squares)
# squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
# print(squares)
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# first_names = [name.split()[0].lower() for name in names]
# print(first_names)
# multiples_3 = [n*3 for n in range(1, 21)]
# print(multiples_3)
# scores = {
#              "Rick Sanchez": 70,
#              "Morty Smith": 35,
#              "Summer Smith": 82,
#              "Jerry Smith": 23,
#              "Beth Smith": 98
#           }
#
# passed = [name for name,age in scores.items() if age > 64]
# print(passed)

# 14. functions, lamba, map, filter
# def multiply_f(x, y):
#     return x * y
# print(multiply_f(2, 3))
# multiply_l = lambda x, y: x * y
# print(multiply_l(5, 6))
# num_list = [1, 2, 3]
# nums_plus_one = lambda num: num + 1
# print(list(map(nums_plus_one, num_list)))

# 15. iterators and generators
# def my_range(x):
#     i = 0
#     while i < x:
#         yield i
#         i += 1
# for x in my_range(7):
#     print(x)
# for x in range(7):
#     print(x)
# lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
# def my_enumerate(iterable, start=0):
#     count = start
#     for element in iterable:
#         yield count, element
#         count += 1
# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))
# def chunker(iterable, size):
#     """Yield successive chunks from iterable of length size."""
#     for i in range(0, len(iterable), size):
#         yield iterable[i:i + size]
# for chunk in chunker(range(25), 4):
#     print(list(chunk))
# sq_list = [x**2 for x in range(10)]  # this produces a list of squares
# sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
# print(sq_list)
# print(sq_iterator)
# name = eval(input("Enter your name: "))
# print("Hello there, {}!".format(name))

#names =  input("Enter names separated by commas: ").split(',')
# names =  [name.title() for name in input('Enter names separated by commas: ').split(',')]
# assignments =  input('Enter assignment counts separated by commas: ').split(',')
# grades =  input('Enter grades counts separated by commas: ').split(',')
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

# 16. Errors and Exceptions / Try Statement
# while True:
#     try:
#         x = int(input('enter a number: '))
#         break
#     except:
#         print('\nexcept clause\n')
#     finally:
#         print('\nfinally clause\n')
#
# try:
#     x = int(input('enter a number: '))
# except:
#     print('\nexcept clause\n')
# else:
#     print('\nelse clause')
# finally:
#     print('\nfinally clause\n')
#
# try:
#     x = int(input('enter a number: '))
# except ValueError:
#     print('\nexcept clause\nValue Error')
# except KeyboardInterrupt:
#     print('\nexcept clause\nKeyboard Interrupt')
# else:
#     print('\nelse clause')
# finally:
#     print('\nfinally clause\n')
#
# try:
#     x = int(input('enter a number: '))
# except (ValueError, KeyboardInterrupt):
#     print('\nexcept clause\nValue Error')
# except :
#     print('\nexcept clause\nKeyboard Interrupt')
# else:
#     print('\nelse clause')
# finally:
#         print('\nfinally clause\n')

# 16. Errors and Exceptions / Try Statement
# def party_planner(cookies, people):
#     leftovers = None
#     num_each = None
#     # TODO: Add a try-except block here to
#     #       make sure no ZeroDivisionError occurs.
#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except Exception as e:
#     # except ZeroDivisionError as e:
#         print('\nZeroDivisionError: {}\n'.format(e))
#     return(num_each, leftovers)
#
# # The main code block is below; do not edit this
# lets_party = 'y'
# while lets_party == 'y':
#
#     cookies = int(input("How many cookies are you baking? "))
#     people = int(input("How many people are attending? "))
#
#     cookies_each, leftovers = party_planner(cookies, people)
#
#     if cookies_each:  # if cookies_each is not None
#         message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
#         print(message.format(people, cookies_each, leftovers))
#
#     lets_party = input("\nWould you like to party more? (y or n) ")

# 17. Reading and Writing files
# f = open('c:/test/my_file.txt', 'w')
# f.write('Hello my new file!!!')
# f.close()
# f = open('c:/test/my_file.txt', 'r')
# file_data = f.read()
# f.close()
# print(file_data)
# f = open('c:/test/my_file.txt', 'a')
# f.write('  Hello again!!!')
# f.close()
# f = open('c:/test/my_file.txt', 'r')
# file_data = f.read()
# f.close()
# print(file_data)
# with open('c:/test/my_file.txt', 'w') as f:
#     f.write('new file contents!!!')
# with open('c:/test/my_file.txt', 'r') as f:
#     file_data = f.read()
# print(file_data)
# with open('c:/test/my_file.txt', 'r') as f:
#     print(f.read(3))
#     print(f.read(5))
#     print(f.read())
# with open('c:/test/my_file.txt', 'w') as f:
#     f.write("""
# line 1
# line 2
# line 3
#     """)
# with open('c:/test/my_file.txt', 'r') as f:
#     print(f.read())
# with open('c:/test/my_file.txt', 'r') as f:
#     # or line in f:
#     #     print(line)
#     for line in f:
#         print(line.strip())
# print('hello, hello again'.split(',')[0])

# 18. Importing Local Scripts and if __name__ == '__main__': concept
# import useful_functions as uf
#
# scores = [88, 92, 79, 93, 85]
#
# mean = uf.mean(scores)
# curved = uf.add_five(scores)
#
# mean_c = uf.mean(curved)
#
# print("Scores:", scores)
# print("Original Mean:", mean, " New Mean:", mean_c)
#
# print(__name__)
# print(uf.__name__)
# uf.main()
# import datetime
# print(datetime)

# 19. Favourate Modules
# csv: very convenient for reading and writing csv files
#
# collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
#
# random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
#
# string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
#
# re: pattern-matching in strings via regular expressions
#
# math: some standard mathematical functions
#
# os: interacting with operating systems
#
# os.path: submodule of os for manipulating path names
#
# sys: work directly with the Python interpreter
#
# json: good for reading and writing json files (good for web work)

# 20. Techniques for Importing Modules
# To import an individual function or class from a module:
#     from module_name import object_name
# To import multiple individual objects from a module:
#     from module_name import first_object, second_object
# To rename a module:
#     import module_name as new_name
# To import an object from a module and rename it:
#     from module_name import object_name as new_name
# To import every object individually from a module (DO NOT DO THIS):
#     from module_name import *
# If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.
#     import module_name
# import package_name.submodule_name

# 21. Third-Party Libraries
# Using a requirements.txt File
# Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs, programmers often list a project's dependencies in a file called requirements.txt. This is an example of a requirements.txt file.
#
# beautifulsoup4==4.5.1
# bs4==0.0.1
# pytz==2016.7
# requests==2.11.1
#
# Each line of the file includes the name of a package and its version number. The version number is optional, but it usually should be included. Libraries can change subtly, or dramatically, between versions, so it's important to use the same library versions that the program's author used when they wrote the program.
#
# You can use pip to install all of a project's dependencies at once by typing
#   pip install -r requirements.txt in your command line.
#
# Useful Third-Party Packages
# Being able to install and import third party libraries is useful, but to be an effective programmer you also need to know what libraries are available for you to use. People typically learn about useful new libraries from online recommendations or from colleagues. If you're a new Python programmer you may not have many colleagues, so to get you started here's a list of packages that are popular with engineers at Udacity.
#
# IPython - A better interactive Python interpreter
# requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
# Flask - a lightweight framework for making web applications and APIs.
# Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
# Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
# pytest - extends Python's builtin assertions and unittest module.
# PyYAML - For reading and writing YAML files.
# NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
# pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
# matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
# ggplot - Another 2D plotting library, based on R's ggplot2 library.
# Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
# pyglet - A cross-platform application framework intended for game development.
# Pygame - A set of Python modules designed for writing games.
# pytz - World Timezone Definitions for Python
