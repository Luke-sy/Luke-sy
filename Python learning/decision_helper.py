import random
print('Welcome to Zokam\'s decision helper')
print('Is your decision a (Y/N) question?')
print('Y / N ') 
y_or_no = input()
if(y_or_no == 'Y' or y_or_no == 'y' or y_or_no == 'Yes' or y_or_no == 'YES' or y_or_no == 'yes'):
    print('Ok. What`s your question?')
    myQuestion = input()
    print('Your question is -' + str(myQuestion) + '-')
    theanswer = random.randint(1,2)
    if theanswer == 1:
        print('My answer is: Yes.')
    else:
        print('My answer is: No.')
    print('Ask me why did I choose that answer')
    input()
    print('I don\'t even care what your question was.')
    print('I just choose randomly between \'Yes\' and \'No\'')

else:
    print('Only Y/N questions are available, goodbye')
