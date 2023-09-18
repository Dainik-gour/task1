class FloatStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "underflow"

    def is_empty(self):
        return len(self.stack) == 0

    def display_stack(self):
        print("Stack elements:")
        for item in self.stack:
            print(f"{item:.4f}")

def main():
    stack = FloatStack()

    while True:
        print("\nOptions:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Print all elements")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            try:
                element = float(input("Enter the element to push: "))
                stack.push(element)
            except ValueError:
                print("Invalid input. Please enter a valid float.")
        elif choice == '2':
            popped = stack.pop()
            if popped == "underflow":
                print("Underflow: The stack is empty.")
            else:
                print(f"Popped element: {popped:.4f}")
        elif choice == '3':
            stack.display_stack()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()