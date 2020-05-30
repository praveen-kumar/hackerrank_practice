from collections import namedtuple

# Categories input should have MARKS in it
# A tuple is immutable, it's mostly used in creating an object which is not supposed to be changed later
total_students, categories = (int(input()), input().split())
Student = namedtuple('Student', categories)
marks = [int(Student._make(input().split()).MARKS) for _ in range(total_students)]
print(sum(marks) / len(marks))
