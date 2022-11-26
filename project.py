# Function to print the name of student who stood first after updation in rank
def nameRank(names, marks, updates, n):

    # Array of students
    x = [[0 for j in range(3)] for i in range(n)]
    for i in range(n):

        # Store the name of the student
        x[i][0] = names[i]

        # Update the marks of the student
        x[i][1] = marks[i] + updates[i]

    highest = x[0]
    for j in range(1, n):
        if (x[j][1] >= highest[1]):
            highest = x[j]
    # for finding jump (current rank - previous rank)
    a = []
    for i in range(n):
        a.append(x[i][1])

    b = a.index(max(a))

    z = marks[b]

    sort = sorted(marks, reverse=True)

    Index = sort.index(z)

    # Print the name and jump in rank
    print("Name: ", highest[0], ", Jump: ",
          abs(Index), sep="")


# Names of the students
name_list = []
num_of_students = int(input("Enter number of students: "))
for _ in range(num_of_students):
    name_list.append(input("Enter student's name: "))
print(name_list)


# Marks of the students
marks_list = []
for i in range(num_of_students):
    try:
        marks_list.append(int(input("Enter the marks in order: ")))
    except ValueError:
        print("The provided value is not an integer")

print(marks_list)


# Updates that are to be done
update_list = []
for _ in range(num_of_students):
    try:
        update_list.append(
            int(input("Enter the updation in student's marks in order: ")))
    except ValueError:
        print('The provided value is not an integer')

print(update_list)
# Number of students
n = len(marks_list)

nameRank(name_list, marks_list, update_list, n)




n = len(marks_list)
 
nameRank(name_list, marks_list, update_list, n)
