# Personal Mini-Toolkit
# This program gives the user a menu of simple tools and lets them keep using the toolkit until they choose to quit.

import random


def number_guessing_game():
    """Play a number guessing game with a set number of attempts."""
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("\nWelcome to the Number Guessing Game!")
    print(f"I am thinking of a number from 1 to 20. You have {max_attempts} tries.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            return

        remaining = max_attempts - attempts
        print(f"Attempts left: {remaining}")

    print(f"Sorry! The number was {secret_number}. Better luck next time!")


# This tool lets the user add, view, and mark tasks as done using a list.
def todo_list():
    tasks = []
    print("\nWelcome to your To-Do List!")

    while True:
        print("\nOptions: ")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Remove a task")
        print("5. Exit to menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task added: {task}")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to mark done.")
            else:
                try:
                    task_number = int(input("Enter the task number to mark done: ")) - 1
                    if 0 <= task_number < len(tasks):
                        completed_task = tasks.pop(task_number)
                        print(f"Task completed: {completed_task}")
                    else:
                        print("That task number does not exist.")
                except ValueError:
                    print("Please enter a valid task number.")
        elif choice == "4":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                try:
                    task_number = int(input("Enter the task number to remove: ")) - 1
                    if 0 <= task_number < len(tasks):
                        removed_task = tasks.pop(task_number)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number does not exist.")
                except ValueError:
                    print("Please enter a valid task number.")
        elif choice == "5":
            print("Returning to the toolkit menu...")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


# This tool performs basic arithmetic operations and keeps asking until the user exits.
def simple_calculator():
    print("\nWelcome to the Simple Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Choose an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")

        again = input("Would you like to calculate again? (y/n): ").lower()
        if again != "y":
            print("Leaving the calculator. Returning to the main menu...")
            break


# This tool capitalizes words and formats names or phrases for quick personal use.
def word_capitalizer():
    print("\nWelcome to the Word Capitalizer!")
    phrase = input("Enter a name or phrase: ")
    formatted = phrase.title()
    print(f"Formatted result: {formatted}")


def show_menu():
    print("\n=== Personal Mini-Toolkit ===")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Word Capitalizer")
    print("5. Quit")


def main():
    print("Welcome to your Personal Mini-Toolkit! Let's get started.")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            word_capitalizer()
        elif choice == "5":
            print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
