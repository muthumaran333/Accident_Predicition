# for the nested list and used to find the second minmum number in the list


# stored_area = []
# for i in range (int(input("Enter the number of students : "))):
#     name = input("Enter the students name : ")
#     score = float(input("Enter the scores of the students :"))
#     stored_area.append([name,score])
# print(stored_area)
# sorted_list = sorted(set([score for name,score in stored_area]))
# print("this is the sorted score with the unique values ", sorted_list)
# second_lowest_score = sorted_list[1]
# name_list = [name for name,score in stored_area if score == second_lowest_score]
# name_list.sort()
# for j in name_list:
#     print(j)
#
# n = int(input("Enter the number of students : "))
# student_marks = {}
# for _ in range(n):
#     name, *line = input("enter name and the marks").split() # this used to effectively collect the input from the user and store the first element to the name and rest of the other element to the line...
#     scores = list(map(float, line))  #it convert the line of the mark to the float  by using map function
#     student_marks[name] = scores
#     print(student_marks)
# query_name = input("enter the name to check")
#
# if query_name in student_marks:
#     scores = student_marks[query_name]
#     average = sum(scores) / len(scores)
#     print(f"{average:.2f}")
# else:
#     print("Student not found")


def count_substring(string, sub_string):
    # Debug: Print the input values
    print(f"Input string: '{string}'")
    print(f"Substring to count: '{sub_string}'")

    # Check if sub_string is empty
    if not sub_string:
        print("The substring is empty. Returning 0.")
        return 0

    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        # Debug: Print the current index and substring being compared
        print(f"Comparing string[{i}:{i + len(sub_string)}] = '{string[i:i + len(sub_string)]}' with '{sub_string}'")

        if string[i:i + len(sub_string)] == sub_string:
            count += 1
            # Debug: Print when a match is found
            print(f"Match found at index {i}. Current count: {count}")

    # Debug: Print the final count
    print(f"Total count: {count}")
    return count

string = input("Enter the main string: ").strip()
sub_string = input("Enter the substring to count: ").strip()

count = count_substring(string, sub_string)
print(count)

