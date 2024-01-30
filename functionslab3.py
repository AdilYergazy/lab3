import math
import random


# 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


# 2
def farenheit_to_celsius(farenheit):
    C = (5 / 9) * (farenheit - 32)
    return C


def solve(numheads, numlegs):
    chick = 0
    while numheads != chick + numlegs / 4:
        numlegs -= 2
        chick += 1
    return chick, numlegs / 4
print(solve(35, 94))

def filter_prime(list1):
    list2 = []
    for i, e in enumerate(list1):
        k = True
        for j in range(2, e):
            print(j)
            if e % j == 0:
                k = False
                break
        if k:
            list2.append(e)
    return list2


set1 = set()


def permut(s, step=0):
    for i in range(step, len(s)):
        string_copy = [ch for ch in s]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        r = "".join(string_copy)
        set1.add(r)
        permut(string_copy, step + 1)
    return set1


def revers(s):
    r = s.split()
    g = []
    for i in range(len(r) - 1, -1, -1):
        g.append(r[i])
    return " ".join(g)


def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] and nums[i] == 3:
            return True
    return False


print(has_33(([1, 3, 3])), has_33([1, 3, 1, 3]), has_33([3, 1, 3]))


def spy_game(nums):
    count1, count2, count3 = 0, 0, 0
    for i in range(0, len(nums)):
        if nums[i] == 0 and count2 == 0 and count3 == 0 and count1 == 0:
            count1 += 1
        if nums[i] == 0 and count1 == 1 and count3 == 0 and count2 == 0:
            count2 += 1
        if nums[i] == 7 and count1 == 1 and count2 == 1 and count3 == 0:
            count3 += 1
    if count1 == count2 == count3:
        return True
    return False


def vol(radius):
    volume = radius * radius * math.pi
    return volume


def unique(list1):
    unique_list = []
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def palindrome(string1):
    s = ''
    for i in range(len(string1) - 1, -1, -1):
        s += string1[i]
    return s == string1


def histogram(list1):
    for i in list1:
        print('*' * i)
    return ''


# game
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am of a number between 1 and 20.")

a = -1
b = random.randint(1, 20)
count = 0
while a != b:
    count += 1
    print("Take a guess.")
    a = int(input())
    if a < b:
        print("Your guess is too low.")
    if a > b:
        print("Your guess is too high")
    print()
print(f"Good job, {name}! You guessed my number in {count} guesses!")
