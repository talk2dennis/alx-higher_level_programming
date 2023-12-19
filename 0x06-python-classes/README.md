# 0x06. Python - Classes and Objects
> Python Object Oriented Programming

# TASK

# 0. My first square
> Write an empty class Square that defines a square:
- Test file:
``` #!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 
```

# 1. Square with size
> - Write a class Square that defines a square by: (based on 0-square.py)
> - Private instance attribute: size
> - Instantiation with size (no type/value verification)
> - You are not allowed to import any module
