#Program to display unique vowels present in the given word #using Stack
vowels =['a','e','i','o','u']
word = input("Enter the word to search for vowels :")
Stack = []
for letter in word:
    if letter in vowels:
        if letter not in Stack:
            Stack.append(letter)
print(Stack)
print("The number of different vowels present in",word,"is",len(Stack))

