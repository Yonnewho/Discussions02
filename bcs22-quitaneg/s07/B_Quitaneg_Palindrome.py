class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.data

def palindrome_checker(sentence):
    def clean_sentence(s):
        return "".join(char.upper() for char in s if char.isalnum())

    stack = Stack()
    cleaned_sentence = clean_sentence(sentence)

    for char in cleaned_sentence:
        stack.push(char)

    reversed_sentence = ""
    for char in cleaned_sentence:
        reversed_sentence += stack.pop()

    return cleaned_sentence, reversed_sentence

# Get the sentence from user input
user_sentence = input("Enter a sentence to check for palindrome: ")
cleaned_sentence, reversed_sentence = palindrome_checker(user_sentence)

if cleaned_sentence == reversed_sentence:
    print(f'The sentence "{user_sentence}" is a palindrome. \n ----------------------------------------------------------------')
else:
    print(f'The sentence "{user_sentence}" is not a palindrome. \n ---------------------------------------------------------------')

print(f'For comparison \n "Cleaned Sentence: {cleaned_sentence}" \n "Reversed Sentence: {reversed_sentence}"')

