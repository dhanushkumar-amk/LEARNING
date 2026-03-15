import numpy as np

np.random.seed(40) # for reproducibility means => same random numbers will be generated every time
marks = np.random.randint(10, 101, size=(20, 5)) # 20 students and 5 subjects

print("Marks :\n", marks)

# average by subjects
average_by_subjects = np.mean(marks, axis=0)
print("Average by subjects :\n", average_by_subjects)

# average by students
average_by_students = np.mean(marks, axis=1)
print("Average by students :\n", average_by_students)

# highest and lowest per subjects
highest_per_subjects = np.max(marks, axis=0)
lowest_per_subjects = np.min(marks, axis=0)

print("Highest per subjects :\n", highest_per_subjects)
print("Lowest per subjects :\n", lowest_per_subjects)

# overall class topper
totalMarks = np.sum(marks, axis=1)
print(totalMarks)

topper = np.argmax(totalMarks)
mark = np.max(totalMarks)
print("Topper is student number", topper + 1, "with marks", mark)

# lowest marks
lowest = np.argmin(totalMarks)
mark = np.min(totalMarks)
print("Lowest is student number", lowest + 1, "with marks", mark)


# no of pass per subject and fails per asubject

no_of_passPerSubject = np.sum(marks >= 35, axis=0)
no_of_failPerSubject = np.sum(marks < 35, axis=0)

print("No of pass per subject :", no_of_passPerSubject)
print("No of fail per subject :", no_of_failPerSubject)

# defficulty subject
defficulty = np.argmin(average_by_subjects)
print("Defficulty subject is", defficulty + 1)

# rank student for first 3 students
rank = np.argsort(totalMarks)
print("Rank student is", rank + 1)
