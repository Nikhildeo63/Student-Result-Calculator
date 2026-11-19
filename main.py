name = input("Enter Student Name: ")
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100

print(f"\n--------\nStudent Results\n--------")
print(f"Name: {name}")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")