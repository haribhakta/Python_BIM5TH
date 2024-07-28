class Example:
    def display(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"Integer argument: {args[0]}")
        elif len(args) == 1 and isinstance(args[0], str):
            print(f"String argument: {args[0]}")
        elif len(args) == 2 and all(isinstance(arg, int) for arg in args):
            print(f"Two integers: {args[0]} and {args[1]}")
        else:
            print("Unsupported arguments")

# Usage
ex = Example()
ex.display(10)
ex.display("Hello")
ex.display(10, 20)
ex.display(10, "Hello")
