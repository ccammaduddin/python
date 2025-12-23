#import modules
from  random import randrange as r 
from time import time as t
# ask how many questions user wants
no__of_questions = int(input('How many questions do you want?: '))
max_num =int(input('Highest number used in practice?: '))
#set score start at zero
score = 0
answer_list = []
#loop through number of questions
start = t()
for q in range(no__of_questions):
    num1,num2 = r(1,max_num+1),r(1,max_num+1)
    ans = num1 * num2
    u_ans =int(input(f'{num1} X {num2} = '))
    answer_list.append(f'{num1} X {num2} = {ans} \nYour answer:{u_ans}')
    if u_ans == ans:
        score += 1
    end = t()
print(f'Thank you for playing! \nYou got {score} out of {no__of_questions} ({round(score/no__of_questions*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/no__of_questions,1)}seconds/question)')
for a in answer_list:
    print(a)