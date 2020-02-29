#import random
import random

subjectsList = [["STC",5],["Sat Commn",4],["VLSI",5],["Dig Sig Processing",5],["Data Comp",3],["MicroWave",5]]

def add_new(subjects,subjectsChosen):
    while True:
        random.shuffle(subjects)
        subjectChoice = subjects[0]
        if(subjectChoice[0] not in subjectsChosen):
            break
    subjectChoice[1] -= 1
    if(subjectChoice[1] == 0):
        subjects.remove(subjectChoice)
    return(subjectChoice[0])

def make_day(subjects,dayspan,dayNo):
    print(f"\nday{dayNo}:")
    subjectsChosen = []
    for i in range(dayspan):
        newSubject = add_new(subjects,subjectsChosen)
        subjectsChosen.append(newSubject)
        print(f"subject{i+1}:".ljust(9," ") + str(newSubject))

for i in range(1,10):
    if(i=='2'):
        make_day(subjectsList,2,i)
    else:
        make_day(subjectsList,3,i)
    

    
