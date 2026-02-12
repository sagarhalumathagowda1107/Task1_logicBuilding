
marks = [45,78,90,33,60]

pass_cnt = 0
fail_cnt = 0

for mark in marks:
    if mark >=50:
        pass_cnt += 1
    else:
        fail_cnt += 1

print("Total number of students: ",len(marks))
print("Number of Student passed: ",pass_cnt)
print("Number of students failed ",fail_cnt)