def count_failing(grades):
    count = 0
    for grade in grades:
        if grade < 60:
            count = count + 1
    return count

print("count_failing---------------")
print(count_failing([55, 54, 66, 78, 79]))

def count_act(scores):
    count = 0
    for score in scores:
        if score > 0 and score < 37:
            count = count + 1
    return count

print("count_act---------------")
print(count_act([2, 7, 9, 34, 0, 37]))

def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print("number_sum---------------")
print(number_sum([5, 5, 6, 3]))

def average_act_score(scores):
   count = 0
   total = 0
   for score in scores:
        if score > 0 and score < 37:
            count = count + 1
            total = score + total
   mean = total / count 
   return mean 

print("average-act-score---------------")  
print(average_act_score({ 1, 17, 37}))

def all_true(booleans):
    count = 0
    for boolean in booleans:
        if boolean == True:
            count = count + 1
    if count == len(booleans):
        return True
    else: 
        return False

print("all_true---------------")   
print(all_true([True, True, True]))
print(all_true([False, False, False]))
print(all_true([True, False, True]))

def any_true(booleans):
    for boolean in booleans:
        if boolean == True:
            return True
        else:
            return False

print("any_true---------------")       
print(any_true([True, False, True]))
print(any_true([False, False, False]))
print(any_true([True, True, True]))

def mostly_true(booleans):
    count = 0
    for boolean in booleans:
        if boolean == True:
            count = count + 1
    if count > len(booleans) / 2:
        return True
    else: 
        return False

print("mostly_true---------------")
print(mostly_true([True, False, True]))
print(mostly_true([False, False, False]))
print(mostly_true([True, True, True]))

def has_vowel(characters):
    for character in characters:
        if character in ["a", "e", "i", "o", "u"]:
            return True
        else:
            return False

print("has_vowel---------------")
print(has_vowel(["a", "b", "c"]))
print(has_vowel(["d", "b", "c"]))