# Google-Parser
Parse rezults from Google

# Requirements
__py.ver__ >= Python 3.6.5 and ```pip install bs4 html5lib requests``` 

# Settings
```python
GoogleParser(query,  # What you search, string
	     page  # Parse from n pages, int. If need 1 - leave blank
	     )
```

# Example
Example:  
```python
import GoogleParser

query = "Python"
rez = GoogleParser(query)

for line in rez.output:
    print(line.name)
    print(line.url)
    print(line.desc)
    print("============")
```

Output:  
```
Welcome to Python.org
https://www.python.org/
The official home of the Python Programming Language.
============
Python (programming language) - Wikipedia
https://en.wikipedia.org/wiki/Python_(programming_language)
Python is an interpreted high-level programming language for general-purpose
programming. Created by Guido van Rossum and first released in 1991, Python ...
============
Python Tutorial - W3Schools
https://www.w3schools.com/python/
Click on the "Run example" button to see how it works. Python File Handling. In
our File Handling section you will learn how to open, read, write, and delete files.
============
Python Tutorial - TutorialsPoint
https://www.tutorialspoint.com/python/
Python Tutorial for Beginners - Learn Python in simple and easy steps starting
from basic to advanced concepts with examples including Python Syntax Object ...
============
Python Tutorial: Learn Python For Free | Codecademy
https://www.codecademy.com/learn/learn-python
Learn Python, a powerful language used by sites like YouTube and Dropbox.
Learn the fundamentals of programming to build web apps and manipulate data.
============
PyPI – the Python Package Index · PyPI
https://pypi.org/
The Python Package Index (PyPI) is a repository of software for the Python
programming language.
============
Python · GitHub
https://github.com/python
Repositories related to the Python Programming language - Python.
============
```
