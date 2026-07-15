import sys
from typing import IO


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py")
        return

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file: IO = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return

    print("---")
    content = file.read()
    print(content)
    print("---")

    file.close()
    print(f"File '{file_name}' closed.")

    transformed = ""
    for char in content:
        if char == "\n":
            transformed = transformed + "#\n"
        else:
            transformed = transformed + char
    if len(content) > 0 and content[-1] != "\n":
        transformed = transformed + "#"

    print("Transform data:")
    print("---")
    print(transformed)
    print("---")

    new_file = input("Enter new file name (or empty): ")

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        out_file: IO = open(new_file, "w")
    except OSError as error:
        print(f"Error opening file '{new_file}': {error}")
        return

    out_file.write(transformed)
    out_file.close()
    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    main()