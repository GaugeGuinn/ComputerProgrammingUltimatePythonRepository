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

def count_numbers(number):
    count = 0
    for numbers in number:
        if numbers in "1234567890":
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
            return False
        else:
            prev = letter 
    return True
        

            

print(in_alphabetical_order("abc"))
print(in_alphabetical_order("acb"))

def alternate_case(word):
    next_upper = True
    result = ""
    for letter in word:
        if next_upper == True:
            result = result + letter.upper()
            next_upper = False
        else:
            result = result + letter
            next_upper = True
    return result

print(alternate_case("pyhton"))

def remove_vowels(word):
    result = ""
    for letter in word:
        if letter in "aeiou":
            pass
        else:
            result = result + letter
    return result

print(remove_vowels("hello"))

def to_camel_case(string):
    result = ""
    next_upper = False
    for letter in string:
        if letter == " ":
            next_upper = True
            result = result + letter
        elif next_upper == True:
            result = result + letter.upper()
            next_upper = False
        else:
            result = result + letter
        result = result.strip()


    return result

print(to_camel_case("hello how are you"))

def to_snake_case(string):
    result = string.replace(" ","_")
    return result

print(to_snake_case("hello how are you"))

def without_duplicates(nums):
    prev = ""
    result = []
    for num in nums:
        if num == prev:
            prev = num
        else:
            result.append(num)
            prev = num
    return result

print(without_duplicates([1, 2, 2, 3, 4,]))
            
def filter_valid_act_scores(scores):
    result = []
    for score in scores:
        if score > 0 and score < 37:
            result.append(score)
        else:
            pass
    return result

print(filter_valid_act_scores([0, 37, 20, 24, 32,]))

