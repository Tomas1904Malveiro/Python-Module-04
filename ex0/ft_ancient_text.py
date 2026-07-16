import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
    except OSError as err:
        print(f"Error opening file '{file_name}': {err}")
        return

    print("---")
    print(file.read())
    print("---")

    file.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
