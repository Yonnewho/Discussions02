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

def clean_sentence(s):
    cleaned_sentence = ""
    for char in s:
        # Check for alphanumeric characters
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            cleaned_sentence += char.lower()
    return cleaned_sentence

def is_palindrome(sentence):
    stack = Stack()
    cleaned_sentence = clean_sentence(sentence)

    for char in cleaned_sentence:
        stack.push(char)

    reversed_sentence = ""
    for char in cleaned_sentence:
        reversed_sentence += stack.pop()

    return cleaned_sentence, reversed_sentence

while True:
    # Get the sentence from user input
    user_sentence = input("Enter a sentence to check for palindrome (type 'E' to quit): ")
    
    if user_sentence.lower() == 'e':
        break
    
    cleaned_sentence, reversed_sentence = is_palindrome(user_sentence)

    if cleaned_sentence == reversed_sentence:
        print(f'The sentence "{user_sentence}" is a palindrome.')
    else:
        print(f'The sentence "{user_sentence}" is not a palindrome.')

    print("Cleaned Sentence:", cleaned_sentence)
    print("Reversed Sentence:", reversed_sentence)
