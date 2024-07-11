#1

file = open('append_mode.txt', mode = 'a')
file.write("Some text")

file.close()
#2

file = open('exclusive_metod.txt', 'x')
file.write("Another text")

file.close()

#3
file = open('specific_position.txt' , 'w')
file = open('specific_position.txt', 'r+')
file.write("Another some text")
file.seek(0)
text = file.read()
print(text)

file.close()

#4

file = open('peterrabbit.txt','r')
text = file.read().lower().split()
words = ["example", "all", "word", "up", "did", "him"]
count = {word : 0 for word in words}

for word in text:
    if word in count:
        count[word] += 1

print(count)

file.close()
