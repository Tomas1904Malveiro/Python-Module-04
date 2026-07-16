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


def main():
    print("=== Cyber Archives Security ===")
    print("")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("invalid.txt"))

    print("")
    result = secure_archive("hello.txt")
    print("Using 'secure_archive' to read from a regular file:")
    print(result)

    print("")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_vault_file.txt", "write", result[1]))


if __name__ == "__main__":
    main()
