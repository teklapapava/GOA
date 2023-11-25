# დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.

# რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 1 ქულა და
# გადავალთ შემდეგზე(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)( ანუ remove დაგჭირდებათ),
import random
arr_of_students = ["giorgi","salome","rati","anri","demetre"]
arr_of_grades =[0, 0, 0, 0, 0]
for i in range(5):
    random_student = random.choice(arr_of_students)
    print(random_student)
    answer = input("did the student answer correctly?: ")
    index_of_random_student = arr_of_students.index(random_student)
    if answer == "yes":
        random_students_grade = arr_of_grades[index_of_random_student]
        random_student_grade += 10
        print(random_student, "has plus 10 grade and the next student is: ")
        arr_of_students.remove(random_student)
    elif answer == "no":
        random_student_grade = arr_of_grades[index_of_random_student]
        random_student_grade -= 5
        print("the student has minus 5 grade and the next student is: ")
    else:
        print("yes or no")
print("quiz is over and the students have overall grade",arr_of_grades)