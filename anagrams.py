
def is_anagram(text1, text2):

    hist1 = {}
    hist2 = {}

    for char in text1.lower():
        hist1[char] = hist1.get(char, 0) + 1

    for char in text2.lower():
        hist2[char] = hist2.get(char, 0) + 1


    return hist1 == hist2

print(is_anagram("oko", "koo"))
print(is_anagram("oko", "kko"))