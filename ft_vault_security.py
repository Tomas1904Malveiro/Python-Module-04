def secure_archive(filename, action="read", content=""):
    try:
        if action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:",
          secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:",
          secure_archive("/etc/master.passwd"))

    result = secure_archive("ancient_fragment.txt")
    print("Using 'secure_archive' to read from a regular file:",
          result)

    print("Using 'secure_archive' to write previous content to a new file:",
          secure_archive("new_vault_file.txt", "write", result[1]))


if __name__ == "__main__":
    main()
