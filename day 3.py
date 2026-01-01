name = "John Doe"
qoute = '"The best way to get started is to quit talking and begin doing."'
author = "- Walt Disney"
if "begin" in qoute:
    print(f'{name} once said, {qoute} referenced to {author}')
else:
    print("The quote doesn't match the specific requirement.")

print(author.find("Disney"))
print(author.replace("Walt Disney", "Anonymous"))
print(author.upper())
print(name.isalpha())
print(name.split(" "))
