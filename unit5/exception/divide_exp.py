def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero!")
    except TypeError as e:
        print("Error: Invalid input type!")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution completed")

# Usage
divide(10, 2)  # Normal case
divide(10, 0)  # ZeroDivisionError
divide(10, 'a')  # TypeError
