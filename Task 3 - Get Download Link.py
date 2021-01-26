# Opening file 
file1 = open('Task2/result.txt', 'r')
file2 = open('Task3/result.txt', 'w')
count = 0

def slicer(my_str,sub):
    index=my_str.find(sub)
    if index !=-1 :
        return my_str[index:] 
    else:
        raise Exception('Sub string not found!')
    
# Using for loop 
for line in file1: 
    count += 1
    sentence = line.strip()
    combined = slicer(sentence,'/flash/') + '\n'
    replaced = combined.replace("/flash/","")
    file2.write(replaced)
  
# Closing files 
file1.close()
file2.close()
