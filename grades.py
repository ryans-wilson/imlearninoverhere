def computegrade (score):
    if (fcr > 1):
        return("Fuck Off Overachiever")
    elif (fcr >= 0.9):
        return('A')
    elif (fcr >= 0.8):
        return('B')
    elif (fcr >= 0.7):
        return('C')
    elif (fcr >= 0.6):
        return('D')
    elif (fcr < 0.6):
        return('F')
    else: return ('I have No Idea')
scr = input ("Please Enter a Score From 0.0-1.0 ")
try:
    fcr = float(scr)
except:
    print("404 Error: Please Enter a Valid Number From 0.0-0.1")
    quit()
grade = computegrade (fcr)
print ('Final Grade', grade)