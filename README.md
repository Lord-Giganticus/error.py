# error.py
Port of [this gist](https://gist.github.com/Lord-Giganticus/db95058abbd54b198061902a4f6b6d7c) to normal github for use with .gitmodules
* Usage:
```
from error import error #put this in your import statements at the top of your script.

# handling a input error;
choice = int(input('enter a number:'))
if choice >= 0:
  print(choice)
else:
  error.problem(8, 0)
  
# handling a exception during a try: loop;
try:
  bad_thing
except:
  error.problem(15, 16)
```
* To use in .gitmodules:
Refer to [this repo.](https://github.com/Lord-Giganticus/Python-Modules)
