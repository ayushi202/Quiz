from data import question_data

class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

point=0
total=0
for i in range(0,len(question_data)):   
    total+=1
    q1=Question(question_data[i]["text"],question_data[i]["answer"])
    print("Q"+str(i)+"."+str(q1.text))
    ans=input("Your Answer: ")
    if ans.lower()==q1.answer.lower():
        print("That's Correct!")
        point+=1

    else:
        print("That's Wrong!")
        break
    print(f"{point}/{total}")
print(f"Your Score:{point}/{total}")
  
