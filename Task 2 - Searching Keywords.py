import re

# keyword filter (bad design)
keyword1 = "onmouseout="
keyword2 = ").href="
keyword3 = "document.getElementById("

# Read lines
line_end_chars = "\n"

#open files
file2 = open('Task2/result.txt', 'w')

#initial
count = 0


#read batch files
for i in range(1,277):
    j = str(i)
    file1 = open('Task1/page'+ j + '.html', 'r', encoding='utf-8')
    # Using for loop 
    for line in file1: 
        count += 1
        #strip lines
        sentence = line.strip()
        #Regex
        regexPattern = '|'.join(map(re.escape, line_end_chars))
        line_list = re.split(regexPattern, sentence)
        #filter testing
        for line in line_list:
            if keyword1 in line:
                if keyword2 in line:
                    if keyword3 in line:
                        # cut the additional things
                        file2.write(line + "\n")

#remember to close this shit
file1.close()
file2.close()
