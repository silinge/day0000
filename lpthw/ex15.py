from sys import argv

script, filename = argv

txt = open(filename, encoding="utf-8")
print(f"Here is you file {filename}")

print(txt.read())

print("Type the filename again: ")

file_again = input("> " * 5)

txt_again = open(file_again)

print(txt_again.read())