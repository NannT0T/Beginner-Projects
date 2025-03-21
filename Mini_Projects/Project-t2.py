#Name: Madlibs Generator
#Discription: Read a text file <story.txt> into python script and replace <word> in a paragraph with another word that fits in the sentence.
                By using this way, we can change the <word> in the paragraph without discrupting the original one.  

with open(r"C:\Users\ngan1\OneDrive\Documents\Python\Python Projects\Mini_Projects\story-t2.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word + 1: i]
        words.add(word)
        start_of_word = -1
        
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words: 
    story = story.replace(word, answers[word])


print(story) 
