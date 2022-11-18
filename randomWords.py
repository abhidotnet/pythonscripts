import io
import random

f = open("2CITIES.txt", "rb")
content_array = []
word_list = []
sentence = ''
while(True):
	#read next line
    line = f.readline()
    content_array.append(line)
	#if line is empty, you are done with all lines in the file
    if not line:
        break
    #you can access the line
    #print(line.strip())
#close file
f.close
#(len(content_array))
for x in content_array:
    word_list.extend(x.split())
    
#print(len(word_list))
for i in range(1,6):
    rno = random.randrange(1,len(word_list),5)
    sentence = sentence + ' ' + str(word_list[rno],'UTF-8') + ' '
print(str(sentence))

for b in range(1,10):
    rno2 = random.randrange(1,len(content_array))
    secondsen = str(content_array[rno2],'UTF-8')
    print(str(secondsen))