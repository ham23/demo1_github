'''
Python Homework 1
Hillary Miller
22 Feb 2016

Directions:
write and use your own sum function (call it my_sum)
that does not use the built-in sum function in any way

For each row, it will then print to the screen:

Row1: theSum
Row2: theSum
Row3: theSum etc. for as many rows as needed

Note: row numbers in the output begin with 1.

You may not assume any particular number of columns or rows in the data
- the program should work on any sized table of data.
You may use either one of the programs we wrote in class to generate test data.
Advice: use unequal numbers of rows and columns so you can be sure you are doing the right thing
- this will be more important in the next assignment.

Do not put off doing this
- it is short and simple to make sure everyone can get through the basic process
of writing a program including defining and calling a function.
Seek help early if you are having trouble getting it to run successfully.
'''

from __future__ import division, print_function
import sys

def catStr4Print(countLine, sumRes):
    '''
    groups sum result into correct format in string to print
    '''
    outString = 'Row' + str(countLine + 1) + ': ' + str(sumRes)
    return outString

def my_sum(floatsList):
    '''
    sum up a list using for-loop
    '''
    floatSum = 0
    nCols = len(floatsList)
    for x in floatsList: 
        floatSum += x
    return floatSum

def strLineToFloats(inLine):
    '''
    break up a string of a single line from the file into a list of floats
    '''
    floats_line = inLine.split()
    floats_line = map(float, floats_line)
    return floats_line

def main():
    '''
    main program: get the arguments (input file name); call functions 
    '''
    inFileName = sys.argv[1]
    with open(inFileName) as inFile:
        inLines = inFile.readlines()
    for i in range(0, len(inLines)):
        print(catStr4Print(i, my_sum(strLineToFloats(inLines[i]))))
    pass

if __name__ == '__main__':
	main()