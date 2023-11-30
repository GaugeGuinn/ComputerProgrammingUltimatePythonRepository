def count_failing(grades):
    count = 0
    for grade in grades:
        if grade < 60:
            count = count + 1
    return count

print(count_failing([55, 54, 66, 78, 79]))

def count_act(scores):
    count = 0
    for score in scores:
        if score > 0 and score < 37:
            count = count + 1
    return count

print(count_act([2, 7, 9, 34, 0, 37]))

def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

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

   
print(average_act_score({ 1, 17, 37}))




    