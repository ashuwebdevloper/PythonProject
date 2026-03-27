HISTORY_FILE = "history.txt"

def show_history():
    try:
        # Use 'with' to automatically close files even if an error occurs
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No history found!")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No history found!")

def clear_history():
    with open(HISTORY_FILE, "w") as file:
        pass # Just opening in 'w' mode clears the file
    print("History cleared!")

# Fixed: Added 'result' parameter and used correct variable names
def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: 5 + 5")
        return

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operator")
            return
        
        # Format result to remove .0 if it's a whole number
        if result == int(result):
            result = int(result)

        print("Result:", result)
        # Fixed: Pass both the input string and the result
        save_to_history(user_input, result)
        
    except ValueError:
        print("Error: Please enter valid numbers.")

def main():
    print("Simple Calculator (type 'history', 'clear', or 'exit')")
    while True:
        user_input = input("\nEnter calculation (e.g., 2 + 2) or command: ").strip().lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input == "":
            continue
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()