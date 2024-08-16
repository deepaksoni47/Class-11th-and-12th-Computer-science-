#Program to read data from data file in append mode
af=open("test.txt",'a')
lines_of_text = ("One line of text here”,\
    “and another line here”,\
    “and yet another here”, “and so on and so forth")
af.writelines('\n' + lines_of_text)
af.close()
