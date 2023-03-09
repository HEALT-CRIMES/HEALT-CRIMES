#Start by storing the following paragraph in a variable named text:
#Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
#On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth.
#The highest daylight temperature of the Moon is 127 C.
# Enter code below
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. 
There are several interesting facts about the Moon and how it affects life here on Earth. On average,
the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. T
he highest daylight temperature of the Moon is 127 C."""
print(text)

#Your code should resemble the following:

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about 
the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. 
This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Separate the paragraph into sentences
#In English each sentence ends with a period. You will use this to break the paragraph into difference sentences. 
#Using the split method to split the text into sentences by looking for the string . (a period followed by a space).
#Store the result in a variable named sentences. Print the result.
# Enter code below
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('. ')
print(sentences)

#Find keywords
#You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. 
#For each sentence, search for the word temperature. If the word is found, print the sentence.

# Enter code below:
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. 
There are several interesting facts about the Moon and how it affects life here on Earth.
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. 
The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('. ')
for sentence in sentences:
    if "temperature" in sentence: 
        print(sentence)
