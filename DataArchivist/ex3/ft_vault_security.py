#!/usr/bin/env python3

def secure_archive(filepath: str,
                   action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "w":
            with open(filepath, mode="w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filepath, mode="r") as f:
                data = f.read()
            return (True, data)
    except Exception as e:
        return (False, f"{e}")


def main():
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    res = secure_archive("ft_vault_security.py")
    print(res)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "w", res[1]))


if __name__ == "__main__":
    main()
