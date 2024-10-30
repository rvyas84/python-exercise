phone = input('Phone: ')
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    ":(": "😔",
    ":)": "😁"
}

words = phone.split(" ")
print(words)

output = ""

for ch in words:
    output += digit_mapping.get(ch, ch) + " "

print(output)