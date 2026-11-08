# Module 11 Problem 2 - Exam total and average using a function

def compute_scores(exam1, exam2, exam3):
    total = exam1 + exam2 + exam3
    average = total / 3
    return total, average

last_name = input("Enter student's last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))

total, average = compute_scores(exam1, exam2, exam3)

print("Last name:     ", last_name)
print("Total points:  ", format(total, ".1f"))
print("Average score: ", format(average, ".1f"))