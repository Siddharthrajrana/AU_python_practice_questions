def format_text(text):
    result = ""
    capitalize_next = True
    for char in text:
        if char.isdigit():
            result += "[" + char + "]"
        elif char == ".":
            result += char
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char
    return result

text = "this is a sentence. it has 4 numbers. 123."
formatted_text = format_text(text)

with open("formatted_text.txt", "w") as file:
    file.write(formatted_text)
    
print("Done")
