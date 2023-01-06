# 함수 이름은 변경 가능합니다.

# menu 1
def Menu1(name, score1, score2):
    # 사전에 학생 정보 저장하는 코딩
    stu_List[name] = score(score1, score2)

# menu 2

def Menu2():
    # 학점 부여 하는 코딩
    for stu_score in stu_List.values():
        if stu_score.grade == 0:
            avg = (stu_score.mid + stu_score.final) / 2
            if 90 <= avg :
                stu_score.grade = 'A'
            elif 80 <= avg < 90:
                stu_score.grade = 'B'
            elif 70 <= avg < 80:
                stu_score.grade = 'C'
            else:
                stu_score.grade = 'D'

# menu 3
def Menu3():
    # 출력 코딩
    print()
    print("-" * 31)
    print("name    mid    final    grade")
    print("-" * 31)
    for name, score in stu_List.items():
        print("{:<7}{:>4}    {:>4}    {:>4}".format(
            name, score.mid, score.final, score.grade))

# menu 4
def Menu4(name):
    # 학생 정보 삭제하는 코딩
    del stu_List[name]

# 학생 정보를 저장할 변수 초기화
stu_List = {}

class score:
    def __init__(self, mid, final):
        self.mid = mid
        self.final = final
        self.grade = 0

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    # 입력값 예외 처리
    try:
        int(choice)
    except ValueError:
        choice = 0

    if choice == "1":
        String = input("Enter name mid-score final-score : ")
        if len(String.split()) != 3:
            print("Num of data is not 3!")
            continue
        else:
            name, score1, score2 = String.split()

        if name in stu_List:
            print("Already exist name!")
            continue

        else:
            first = True
            second = True
            try:
                int(score1)
            except ValueError:
                first = False
            else:
                score1 = int(score1)
            try:
                int(score2)
            except ValueError:
                second = False
            else:
                score2 = int(score2)
            if first and second:
                if score1 <= 0:
                    first = False
                if score2 <= 0:
                    second = False
                if first and second:
                    Menu1(name, score1, score2)
                else:
                    print("Score is not positive integer!")
            else:
                print("Score is not positive integer!")

    elif choice == "2":
        if len(stu_List) == 0:
            print("No student data!")
        else:
            Menu2()
            print("Grading to all students")

    elif choice == "3":
        if len(stu_List) == 0:
            print("No student data!")
        else:
            Graded = True
            for stu_score in stu_List.values():
                if stu_score.grade == 0:
                    print("There is a student who didin't get grade.")
                    Graded = False
                    break
            if Graded:
                Menu3()

    elif choice == "4":
        if len(stu_List) == 0:
            print("No student data!")
        else:
            name = input("Enter the name to delete : ")
            if name in stu_List:
                Menu4(name)
                print(name, "student information is deleted.")
            else:
                print("Not exist name!")

    elif choice == "5":
        print('Exit Program!')
        break

    else:
        # "Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")