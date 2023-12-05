def is_alliteration(word1,word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False
    
print (is_alliteration("hi","hello"))
print (is_alliteration("boat","joe"))

def count_vowels(word):
    count = 0
    for vowels in word:
        if vowels in "aeiou":
            count = count + 1
    return count

print(count_vowels("Elliot Corriveau"))

def count_numbers(num):
    count = 0
    for digit in num:
        count = count + 1
    return count

print(count_numbers("1000"))

def count_target_letters(word,character):
    count = 0
    for letter in word:
        if character == letter:
            count = count + 1
    return count

print(count_target_letters("hello","l"))

def in_alphabetical_order(word):
    prev = "a"
    for letter in word:
        if letter < prev:
            prev = letter
            return False
        else:
            return True

print(in_alphabetical_order("abc"))
print(in_alphabetical_order("acb"))