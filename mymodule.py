def multiply(a, b):
    return a * b


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def sum_even_numbers(numbers):
    return sum([num for num in numbers if num % 2 == 0])


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)    