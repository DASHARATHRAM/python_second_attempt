student_scores = input().split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
current_max = 0
for score in student_scores:
    if score > current_max:
        current_max = score

print(current_max)