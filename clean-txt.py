import sys
import os
import mimetypes


def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: python clean-text.py <path_to_file>")
        sys.exit(1)  # Return non-zero status code

    # Get the file path from command line argument
    file_path = sys.argv[1]

    # Validate the file is a plain text file
    validate_file(file_path)

    # Determine destination path using the file name
    dest_path = get_dest_path(file_path)

    # Process the file
    process_file(file_path, dest_path)

    print(f"SUCCESS! Created new file at {dest_path}")


def validate_file(file_path: str) -> None:
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' does not exist.")
        sys.exit(1)  # Return non-zero status code

    # Guess the MIME type of the file
    mime_type, encoding = mimetypes.guess_type(file_path)
    if mime_type is None or not mime_type.startswith('text'):
        print(
            f"The file '{file_path}' does not appear to be a plain text file (MIME type: {mime_type}).")
        sys.exit(2)  # Return non-zero status code


def get_dest_path(file_path: str) -> str:
    filename_with_extension = os.path.basename(file_path)
    filename_without_extension = os.path.splitext(filename_with_extension)[0]

    return f"output/{filename_without_extension}.cleaned.txt"


def process_file(source_file: str, dest_file: str) -> None:
    """Read the content of the file, remove commas, and write it back."""
    try:
        with open(source_file, 'r') as file:
            content = file.read()

        new_content = content.replace(',', '')
        new_content = new_content.replace(' ', '\n')

        with open(dest_file, 'w') as file:
            file.write(new_content)

    except Exception as e:
        print(f"Error processing the file: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()
