import csv

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()


def most_vowels(words):
    most = ""
    max_vowel = 0
    count = 0
    for word in words:
        count = 0
        for letter in word:
            if letter in "aeiou":
                count = count + 1
                if count > max_vowel:
                    max_vowel = count
                    most = word
    return most, max_vowel

print(most_vowels(words))



def find_average_length(words):
    count = 0
    total = 0
    final = 0
    for word in words:
        total = total + len(word)
        count = count + 1
    final = total / count
    final = round(final,2)


    return final

print(find_average_length(words))


f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)

def find_grades(reader):
    a = 0
    b = 0 
    c = 0
    d = 0
    f = 0
    for row in reader:
        name, gradelevel, percent = row
        percent = int(percent)
        if percent > 89:
            a = a + 1
        elif percent > 79:
            b = b + 1
        elif percent > 69:
            c = c  + 1
        elif percent > 59:
            d = d + 1
        else:
            f = f + 1
    return "A:",a,"B:",b,"C:",c,"D:",d,"F:",f

print (find_grades(reader)) 

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
def average_grades(reader):
    frcount = 0 
    frtotal = 0
    socount = 0
    sototal = 0
    jrcount = 0
    jrtotal = 0
    srcount = 0
    srtotal = 0
    fr_average = 0
    so_average = 0
    jr_average = 0
    sr_average = 0
    for row in reader:
        name, gradelevel, percent = row
        gradelevel = int(gradelevel)
        percent = int(percent)
        if gradelevel == 9:
            frtotal = frtotal + percent
            frcount = frcount + 1
            fr_average = frtotal / frcount
            

        if gradelevel == 10:
            sototal = sototal + percent
            socount = socount + 1
            so_average = sototal / socount

        if gradelevel == 11:
            jrtotal = jrtotal + percent
            jrcount = jrcount + 1
            jr_average = jrtotal / jrcount

        if gradelevel == 12:
            srtotal = srtotal + percent
            srcount = srcount + 1
            sr_average = srtotal / srcount
    fr_average = round(fr_average, 2)
    so_average = round(so_average, 2)
    jr_average = round(jr_average, 2)
    sr_average = round(sr_average, 2)
    return  fr_average, so_average, jr_average, sr_average


print(average_grades(reader))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
def failing_seniors(reader):
    
    for row in reader:
        name, gradelevel, percent = row
        gradelevel = int(gradelevel)
        percent = int(percent)
        if gradelevel == 12 and percent < 60:
            print(name)
    return ""


print(failing_seniors(reader))       

        


