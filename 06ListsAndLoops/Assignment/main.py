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

def all_the_same(nums):
    count = 0
    numsTrue = 0
    while count == 0:
        for num in nums:
            if num == nums[0]:
                numsTrue = numsTrue + 1
            else:
                count = count + 1
                return False
            if numsTrue == len(nums):
                return True
           
print("all_the_same---------------")
print(all_the_same(["2", "2", "2"]))
print(all_the_same(["1", "2", "3"]))

def increasing(nums):
    greatest = nums[0]
    count = 1
    for num in nums:
        if greatest < num:
            greatest = num
            count = count + 1
    if count == len(nums):
         return True
    else:
         return False
        
print("increasing---------------")
print(increasing(["2", "2", "2"]))
print(increasing(["1", "2", "3"]))

def is_incrementing(nums):
    number = nums[0]
    for num in nums:
        if num == number + 1:
            return True
    else: 
        return False

print("is_incrementing---------------")
print(is_incrementing([2,2,2]))
print(is_incrementing([1,2,3]))

def has_adjacent_repeat(nums):
    prev = 9999999999
    for num in nums:
        if num == prev:
            return True
        else:
            prev = num
    else:
        return False
print("has_adjacent_repeat---------------")
print(has_adjacent_repeat([2,2,2]))
print(has_adjacent_repeat([1,2,3]))

def sum_with_skip(nums):
    skip = False
    total = 0
    for num in nums:
        if num == -1 and skip == True:
            skip = False
        elif num == -1 and skip == False:
            skip = True
        elif skip == False:
            total = num + total
    return total

print("sum_with_skip---------------")
print(sum_with_skip([1,2,-1,1,-1,2]))