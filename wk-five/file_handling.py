# file_handling.py
import os


def create_file():
    """
    Creates a file 'file.txt' and writes initial content, but only if the file does not already exist.
    """
    try:
        # Check if the file exists
        if os.path.exists("file.txt"):
            print(
                "File 'file.txt' already exists. Skipping creation to avoid overwriting."
            )
            return

        # Create and write to the file only if it does not exist
        with open("file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line, including a number: 123.\n")
            file.write("Final line with some text and a number: 456.\n")
        print("File created and initial content written successfully.")

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def read_file():
    """
    Reads and displays the content of 'file.txt'.
    """
    try:
        with open("file.txt", "r") as file:
            content = file.read()
            print("\nReading from 'file.txt':\n")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def append_to_file():
    """
    Appends additional content to 'file.txt'.
    """
    try:
        with open("file.txt", "a") as file:
            # Write additional lines to the file
            file.write("This is an appended line: additional content 789.\n")
            file.write("Another appended line with more text.\n")
            file.write("Final appended line with the number: 101.\n")
        print("Content appended successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to perform file creation, reading, and appending with error handling.
    """
    try:
        create_file()  # Step 1: Create and write initial content
        read_file()  # Step 2: Read and display content
        append_to_file()  # Step 3: Append additional content
        read_file()  # Step 4: Read and display updated content
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")


# Run the main function
if __name__ == "__main__":
    main()
