import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{file_name}': {error}",
              file=sys.stderr)
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

    print("")
    print("Transform data:")
    print("---")
    print(transformed)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline()

    if new_file[-1:] == "\n":
        new_file = new_file[:-1]

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")

    try:
        out_file = open(new_file, "w")
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
