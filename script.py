def sum(a, b):
    return a+b
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is forbidden")
   if isinstance(a, str) or isinstance(b, str):
       raise ValueError("Could not devide strings")
  if isinstance (a, list) or isinstance(b, list):
       raise LalueError("Could not divide lists")
    return a/b
