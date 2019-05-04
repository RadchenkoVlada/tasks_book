"""
Exercise 5:

Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after
the colon character and then use the float function to convert the extracted string into a floating point number.
"""

def converting_to_float():
    line = 'X-DSPAM-Confidence:0.8475'
    atpos = line.find(":")
    print(atpos)
    after_pos = line[atpos + 1:]
    number = float(after_pos)
    print(number)
    print(type(number))



if __name__ == '__main__':
    converting_to_float()
