### This Python script reads a .txt file, count things in the file, and output a new txt file

# Read the txt file
fhand = open('exercise-files/romeo-full.txt')

# Define variables to count things
count = 0 # count lines
# more variables to count other things

# Loop through each line to count things
for line in fhand:
    count = count + 1
    # more code to count things
    if line.startswith('ROMEO'):
        count_Romeo = count_Romeo + 1
    if line.startswith('JULIET'):
        count_Juliet = count_Juliet + 1



# Create an output.txt file
fout = open('output.txt', 'w')
fout.write('Line of text: ' + str(count) + '\n')
fout.write('Romeo: ' + str(count_Romeo) + '\n')
fout.write('Juliet: ' + str(count_Juliet) + '\n')

# Close the file
fout.close()
