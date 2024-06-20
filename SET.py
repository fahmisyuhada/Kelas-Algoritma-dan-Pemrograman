paragraf = "saya pergi ke pasar, saya ketemu bapak saya"
split = paragraf.split()
print(split)
# create a set of integer type
student_id = {112, 114, 112, 116, 118, 115, 114, 116,114, 101, 100}
print('Student ID:', student_id)
data = {}
setSplit = set(split)
print(type(setSplit))
print(type(paragraf))
print(type(split))
print(type(student_id))
print(type(data))
student_id.add(212)
student_id.add(212)
print(student_id)
student_id.discard(115)
for i in student_id:
    print(i)
print(list(enumerate(student_id)))
print(max(student_id))
print(min(student_id))
print(sum(student_id))
print(sorted(student_id))

# first set
A = {1, 3, 5, 2}

# second set
B = {0, 2, 4, 7, 3}

unionAB = A.union(B)  # A|B
print(unionAB)

intsec = A&B
print(intsec)

diffAB = A - B
print(diffAB)
diffBA = B-A
print(diffBA)
simDeffAB = A.symmetric_difference(B)
print(simDeffAB)

# first set
A = {1, 3, 5}

# second set
B = {3, 5, 0}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')