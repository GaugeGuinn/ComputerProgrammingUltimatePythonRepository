def make_abc():
    return ["a, b, c"]
print("Demonstrate make_abc ", make_abc())

def equal_edges(integers):
    first = integers[0]
    last = integers[-1]
    if int(first) == int(last):
        return True
    else:
        return False
print("equal_edges:")
print("1, 2, 3, 4, 1 ==>", equal_edges("1, 2, 3, 4, 1"))
print("5, 6, 7, 8, 9 ==>", equal_edges("5, 6, 7, 8, 9"))

def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1 [-1]
    last2 = list2 [-1]

    if first1 == first2 or first1 == last2:
        return True
    if last1 == first2 or last1 == last2:
        return True
    else: return False
print("common_edge:")
print("[1, 2, 3, 4], [5, 6, 7, 8] ==>", common_edge([1, 2, 3, 4], [5, 6, 7, 8]))
print("[1, 2, 3,], [3, 4, 5] ==>", common_edge([1, 2, 3,], [3, 4, 5]))

def all_the_same(integers):
    first, middle, last = integers
    if first == middle and first == last:
        return True
    if middle == first and middle == last:
        return True
    if last == first and last == middle:
        return True
    else:
        return False
print("all_the_same:")
print("[1, 2, 3]", all_the_same([1, 2, 3,]))
print("[5, 5, 5]", all_the_same([5, 5, 5,]))   

def all_unique(integers):
    first, middle, last = integers
    if first != middle and first != last:
        return True
    if middle != first and middle != last:
        return True
    if last != middle and last != first:
        return True
    else:
        return False
print("all_unique:")
print("[1, 2, 3]", all_unique([1, 2, 3]))
print("[5, 5, 5]", all_unique([5, 5, 5]))

def increasing(integers):
    first, middle, last = integers
    if first < middle and middle < last:
        return True
    else:
        return False

print("increasing:")
print("[1, 2, 3]", increasing([1, 2, 3]))
print("[5, 5, 5]", increasing([5, 5, 5]))

def all_true(booleans):
    first, middle, last = booleans
    if first == True and middle == True and last == True:
        return True
    else:
        return False

print("all_true:")
print("[true, false, true]", all_true([True, False, True]))

def mostly_true(booleans):
    first, middle, last = booleans
    if first == True and middle == True:
        return True
    if middle == True and last == True:
        return True
    if first == True and last == True:
        return True
    else: 
        return False
print("mostly_true:")
print("[True, False, False]", mostly_true([True, False, False]))
print("[False, False, False]", mostly_true([False, False, False]))

def make_copy(integers):
    copy = integers 
    return copy
print(make_copy([5, 6, 1]))

def repeat_thrice(integer):
    repeat = [integer, integer, integer]
    return repeat
print(repeat_thrice(3))

def make_reversed_copy(integers):
    first, middle, last = integers
    reverse = [last, middle, first]
    return reverse
print(make_reversed_copy([1, 2, 3]))

def reverse_in_place(integers):
    [first, middle, last] = integers
    integers = [last, middle, first]
    return integers
print(reverse_in_place([1, 2, 3]))