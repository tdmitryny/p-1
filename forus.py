student_heights = input("List of students heights ").split()
print(student_heights)

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    



#print(student_heights)

total_heights = 0
for heights in student_heights:
    total_heights += heights
    

#print(total_heights)

students = 0
for num_students in student_heights:
    students += 1
#print(students)

average = round(total_heights / students)
print(f"The avearge is {average}")




#156 178 165 171 187