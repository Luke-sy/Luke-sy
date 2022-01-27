print('Hello there')
print('Please put your name:')
myName = input()
if(len(str(myName)) > 8):
    print('Woah. You got exited writing your name, didn\'t you?')
else:
    print('Short. Direct. Nice')
print('Hello ' + myName + ', I hope you are fine')
print('And... How old are you?')
myAge = input()
if(int(myAge) < 16):
    print('Ohhh nice, you are a kiddo')
elif(int(myAge) < 18):
    print('Well, you are roughly an adult')
elif(int(myAge) < 21):
    print('I guess you are not able to drink in the US, eh?')
elif(int(myAge) < 28):
    print('I guess we share "Age range". Uh?')
else:
    print('Hey there, granny')

 