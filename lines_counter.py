fh = open('C:/Users/Anoux/.spyder-py3/python_coding/brown_butter_brownies','r')

count = 0
for line in fh:
    # print(line.strip()) """ if I want to print each line besides counting it
    count = count + 1
    
print("There are " + str(count) + " lines in the txt file")