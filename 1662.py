word1 = ["ab", "c"]
word2 = ["a", "bc"]


# str1 = ""
# str2 = ""
# for i in range(len(word1)):
#     str1 += word1[i]
# for i in range(len(word2)):
#     str2 += word2[i]

# return str1 == str2


def conj():
    return bool("".join(word1) == "".join(word2))
