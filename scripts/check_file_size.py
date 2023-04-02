import os
import sys


def main():
    max_file_size = 100 * 1024  # 100 KB
    error = False

    for file_path in sys.argv[1:]:
        file_size = os.path.getsize(file_path)
        if file_size > max_file_size:
            print(f"ERROR: {file_path} is too large ({file_size / 1024} KB)")
            error = True

    if error:
        sys.exit(1)


if __name__ == "__main__":
    main()
