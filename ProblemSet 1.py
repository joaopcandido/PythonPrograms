'''
PROBLEM 1:
	Assume s is a string of lower case characters.
	Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
'''
count=0
for letter in s:
    if (letter == 'a')|(letter == 'e')|(letter == 'i')|(letter == 'o')|(letter == 'u'):
        count += 1

print('Number of vowels: ' + str(count))


'''
PROBLEM 2:
	Assume s is a string of lower case characters.
	Write a program that prints the number of times the string 'bob' occurs in s.
'''
count = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        count += 1
    if i + 3 == len(s):
        break;
        
print('Number of times bob occurs is: ' + str(count))


'''
PROBLEM 3:
	Assume s is a string of lower case characters.
	Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

	For example, if s = 'azcbobobegghakl', then your program should print:		Longest substring in alphabetical order is: beggh
	In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
		Longest substring in alphabetical order is: abc
'''
answer = ''
aux = ''

for i in range(len(s) - 1):
    if aux == '':
        aux += s[i]
    if s[i] <= s[i+1]:
        aux += s[i+1]
    if len(answer) < len(aux):
        answer = aux
    if s[i] > s[i+1]:
        aux = ''

print('Longest substring in alphabetical order is: ' + answer)