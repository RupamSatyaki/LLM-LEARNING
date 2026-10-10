def calculateGrade(fullMarks, obtainedMarks):
    percentage = (obtainedMarks / fullMarks) * 100
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80 and percentage < 90:
        grade = "A"
    elif percentage >= 70 and percentage < 80:
        grade = "B+"
    elif percentage >= 60 and percentage < 70:
        grade = "B"
    elif percentage >= 50 and percentage < 60:
        grade = "C"
    elif percentage >= 40 and percentage < 50:
        grade = "D"
    elif percentage < 40:
        grade = "F"
        
    return percentage, grade

def calculateResult (grade):
    if grade == "F":
        result = "FAIL"
    else :
        result = "PASS"
        
    return result

def getStudentDetails():

    # validate student name is only contains alphabets and spaces
    while True:
        studentName = input("Enter your Full Name: ")

        if studentName.replace(" ","").isalpha():
            break
        else:
            print("Invalid name! Please enter only alphabets and spaces.")


    # validate Obtained Marks is only contains numbers
    while True:
        obtainedMarksInput = input("Obtained Marks: ")

        if obtainedMarksInput.isdigit():
            obtainedMarks = int(obtainedMarksInput)
            break
        else:
            print("Invalid input! Obtained Marks must contain only numbers.")


    # validate Full Marks is only contains numbers
    while True:
        fullMarksInput = input("Full Marks: ")

        if fullMarksInput.isdigit():
            fullMarks = int(fullMarksInput)
            break
        else:
            print("Invalid input! Full Marks must contain only numbers.")
    
    
    
    calculate_grade = calculateGrade(fullMarks, obtainedMarks)
    percentage = calculate_grade[0]
    grade = calculate_grade[1]
    
    
    result = calculateResult(grade)

    return studentName, obtainedMarks, fullMarks, percentage, grade, result


def getLoanDetails ():

    while True:
        ageInput = input("Enter your age: ")

        if ageInput.isdigit():
            age = int(ageInput)

            if age >= 18 and age <= 35:
                break
            else:
                print("Invalid age! Age must be between 18 and 35.")
        else:
            print("Invalid input! Age must contain only numbers.")

    while True:
        admissionStatus = input("Your Admission status(Confirmed/Not confirmed): ").strip().lower()

        if admissionStatus == "confirmed" or admissionStatus == "not confirmed":
            break
        else:
            print("Invalid input! Please enter only Confirmed or Not Confirmed.")


    while True:
        loanAmountInput = input("Loan amount: ")

        if loanAmountInput.isdigit():
            loanAmount = int(loanAmountInput)

            if loanAmount <= 750000:
                break
            else:
                print("Invalid Loan Amount! Loan Amount must be under 7,50,000.")
        else:
            print("Invalid input! Loan Amount must contain only numbers.")
    
    return age, admissionStatus, loanAmount


def loan_eligibality(loanDetails, result, percentage):
    
    # break details
    age = loanDetails[0]
    admissionStatus = loanDetails[1]
    loanAmount = loanDetails[2]
    
    # check eligibality
    if age >= 18 and age <= 35:
        if result == "PASS":
            if percentage >= 50:
                if admissionStatus == "confirmed":
                    if loanAmount <= 750000:
                        eligiblityStatus = "True"
                    else:
                        print("maximum loan amount is 750000, please restart the application")
                else:
                    print("Your admission status is not confirmed yet")
            else:
                print("minimum percentage requirment for the loan is 50%")
        else:
            print("minimum percentage requirment for the loan is 50%")
    else:
        print("Age requirement for the student loan between 18 and 35")
        
    return eligiblityStatus
    
def recieptGenerator(studentName, obtainedMarks, fullMarks, percentage, grade, result, age, admissionStatus, loanAmount):
    
    
    print("=" * 40)
    print("        STUDENT REPORT RECEIPT")
    print("=" * 40)
    print(f"Student Name      : {studentName}")
    print(f"Obtained Marks    : {obtainedMarks}")
    print(f"Full Marks        : {fullMarks}")
    print(f"Percentage        : {percentage:.2f}%")
    print(f"Grade             : {grade}")
    print(f"Result            : {result}")
    print("-" * 40)
    print("        LOAN DETAILS")
    print("-" * 40)
    print(f"Age               : {age}")
    print(f"Admission Status  : {admissionStatus}")
    print(f"Loan Amount       : Rs. {loanAmount:.2f}")
    print("=" * 40)
    print("      Thank You! Visit Again")
    print("=" * 40)
    
    
    

def main():
    details = getStudentDetails()
    
    studentName = details[0]
    obtainedMarks = details[1]
    fullMarks = details[2]
    percentage = details[3]
    grade = details[4]
    result = details[5]

    
    print("-----Hi! " + details[0] + ", check your details bellow-----")
    
    # print all information of student
    print("STUDENT NAME: ", details[0])
    print("OBTAINED MARKS: ", details[1])
    print("FULL MARKS: ", details[2])
    print("PERCENTAGE: ", details[3])
    print("GRADE: ", details[4])
    print("RESULT: ", details[5])
    
    
    # ask if student want to apply for a loan
    askForLoan = str(input("Would you like to apply for student loan(YES/NO): "))
    
    if askForLoan == "yes" or askForLoan =="YES":
        
        # get loan details from student
        loanDetails = getLoanDetails()
        
        age = loanDetails[0]
        admissionStatus = loanDetails[1]
        loanAmount = loanDetails[2]
        
        # check loan eligiblity 
        eligiblityStatus = loan_eligibality(loanDetails, result, percentage)
        
        # check eligiblity
        if eligiblityStatus == "True":
            print("Loan Status: Eligible")
            print("Loan Approved")
            print("check your loan reciept bellow")
            
            recieptGenerator(studentName, obtainedMarks, fullMarks, percentage, grade, result, age, admissionStatus, loanAmount)
        else:
            print()



main()