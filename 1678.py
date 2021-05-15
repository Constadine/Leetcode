command = "G()(al)"

final = ""
for char in range(len(command)):
    if command[char] == "G":
        final += "G"
    if command[char] == "(":
        if command[char + 1] == ")":
            final += "o"
        elif command[char + 1] == "a":
            final += "al"

return final

# or

return command.replace("()", "o").replace("(al)", "al")
