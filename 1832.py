import string

sentence = "thequickbrownfoxjumpsoverthelazydog"


def ok():
    for letter in list(string.ascii_lowercase):
        if letter not in sentence:
            return False
    else:
        return True


print(ok())
