marks=[53,63,22,12,66,22,72,89,36,93]

def grade(marks):

    if marks > 90:

        return "A"
    
    elif 80 <=marks <90:

        return "B"
    
    elif 70 <=marks <80:

        return "C"
    
    elif 60 <=marks <70:

        return "D"
    
    else:

        return "Fail"
    

grades=map(grade,marks)
#grades=list(map(grade,marks))

print("Exam Score=>",marks)

# print("Grade=>",next(grades))
print("Grade=>",list(grades))

