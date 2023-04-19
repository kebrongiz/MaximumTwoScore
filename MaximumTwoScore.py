def student_max_two_score():
    student_no = int(input("Enter the number of students: "))

    scores = {}

    for _ in range(student_no):
        print()
        name = input("Enter student name: ")
        score = int(input("Enter student score: "))

        if scores.get(score) is None:
            scores[score] = []

        scores[score].append(name)
    sorted_scores = sorted(scores)
    sorted_scores.reverse()
    max_score = sorted_scores[0]
    max_score_students = ", ".join(scores.get(max_score))
    second_max_score = sorted_scores[1]
    second_max_score_students = ", ".join(scores.get(second_max_score))

    print()
    print("The student(s) with the highest score is/are {} with a score of {}".format(
        max_score_students, max_score))
    print("The student(s) with the second highest score is/are {} with a score of {}".format(
        second_max_score_students, second_max_score))


student_max_two_score()
