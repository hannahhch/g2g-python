#comprehensions are like map or filter

words = ["file", "apple", "directory", "banana"]

#strings
for word in words:
    print(word[::-1])

#list (array)
reverse_words = []
for word in words:
    reverse_words.append(word[::-1])

print("reverse word list:", reverse_words)

reverse_words = [words[::-1] for word in words]
new_word_list = [word for word in words]

short_word_list = [word
                    for word in words
                    if len(word) < 7]

print("short word list: ", short_word_list)
