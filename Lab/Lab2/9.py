def cal_result(exam1_marks , exam2_marks, sports_marks , act1_marks ,act2_marks, act3_marks):
    exam_marks = (exam1_marks + exam2_marks)/2
    result = ((exam_marks*0.50)+(sports_marks*0.20)+(act1_marks*0.10) + (act2_marks*0.10) + (act3_marks*0.10))
    return result

exam1_marks = float(input("Enter the Marks of First Exam : "))
exam2_marks = float(input("Enter the Marks of Second Exam : "))
sports_marks = float(input("Enter the Marks in Sports  : "))
act1_marks = float(input("Enter the Marks of First Activity : "))
act2_marks = float(input("Enter the Marks of Second Activity : "))
act3_marks = float(input("Enter the Marks of Third Activity : "))

result = cal_result(exam1_marks , exam2_marks, sports_marks , act1_marks ,act2_marks, act3_marks)
print(f"Overall : {result:.2f}")
