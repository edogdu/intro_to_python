'''
asg4.py

Name:
Student ID:

Write the following functions
'''

#f1 (10 pts) return the reverse of str. For example for 'Hello' it returns 'elloH'
def reverse(str):
    rev = ''
    for c in str:
        rev = c + rev
    return rev

#f2 (10 pts) counts a string str in text (case sensitive)
def count(str,text):
    cnt = 0
    for i in range(len(text)):
        if text[i:].startswith(str):
            cnt += 1
    return cnt

#f3 (10 pts) returns True of str is a palindrome or returns False
def palindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

#f4 (10 pts) returns text with the following shortcuts replaced with full text
# omg: Oh my God!
# btw: By the way
# imo: In my opinion
# kiss: Keep it simple stupid!
def full(text):
    return text.replace('omg','Oh my God!').replace('btw','By the way').replace('imo','In my opinion').replace('KISS','Keep it simple stupid!')

#f5 (20 pts) returns text with 3-character long words in the text replaced with * wrapped
# For example, 'My number one priority is ...' is returned as 'My number *one* priority is *...*'
def star(text):
    list = text.split()
    for w in list:
        if len(w) == 3:
            text = text.replace(w,'*' + w + '*')
    return text

#f6 (10 pts) returns the text hidden, where all characters are replace with . except the first and the last character.
def hide(text):
    return text[0] + (len(text)-2)*'.' + text[len(text)-1]

#f7 (10 pts) count the numbers (0..9) in text.
# Hint: '0' < ... < '9'
def digitCount(text):
    cnt = 0
    for c in text:
        if c >= '0' and c <= '9':
            cnt += 1
    return cnt

#f8 (20 pts) Prints numbers (1..num) towards left 'l' or right 'r'
def numbers(num,direction):
    for i in range(num):
        if direction == 'l':
            print(' '*(num-1-i) + str(i+1))
        else:
            print(' '*i + str(i+1))

# tests
'''
print(reverse('Hello'))
print(count('sh','One Fish, Two Fish, Red Fish, Blue Fish'))
print(palindrome('02022020'))
print(full('KISS kiss omg what? ... btw, imo...'))
print(star('My number one priority is ...'))
print(hide('02022020'))
print(digitCount('abc02 02mda 2bmw020'))
numbers(10,'l')
numbers(10,'r')


print(reverse('abcdefG'))
print(count('h','One Fish, Two Fish, Red Fish, Blue Fish'))
print(palindrome('madam'))
print(full('Kiss KISS Omg omg what? ... --btw--, _imo_...'))
print(star('One Fish, Two Fish, Red Fish, Blue Fish'))
print(hide('My secret password'))
print(digitCount('0abc 1def ghi2 3 456'))
numbers(5,'l')
numbers(5,'r')
'''
