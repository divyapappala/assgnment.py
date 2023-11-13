import os
file_path = r"C:\Users\lokes\Desktop\assignment\text.txt"
start_range = 1
end_range = 100

try:
    with open(file_path, "r") as file:
        content = file.read()
        content_range = content[start_range:end_range]
        word_count = len(content_range.split())

        print(f"Content in the specified range: {content_range}")
        print(f"Word count: {word_count}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    with open(file_path, "a") as file:
        file.write("\n" + content_to_write)
        print(f"Content written to the file: {content_to_write}")
except Exception as e:
    print(f"An error occurred: {e}")
