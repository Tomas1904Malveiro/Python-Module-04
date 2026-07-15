import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO = open(filename, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{filename}': {error}",
              file=sys.stderr)
        return

    print("---")
    content = file.read()
    print(content, end="")
    print("---")

    file.close()
    print(f"File '{filename}' closed.")

    transformed = ""
    for char in content:
        if char == "\n":
            transformed += "#\n"
        else:
            transformed += char
    if len(content) > 0 and content[-1] != "\n":
        transformed += "#"

    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline()
    if len(new_file) > 0 and new_file[-1] == "\n":
        new_file = new_file[:-1]

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        out_file: IO = open(new_file, "w")
    except OSError as error:
        print(f"[STDERR] Error opening file '{new_file}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return

    out_file.write(transformed)
    out_file.close()
    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    main()
