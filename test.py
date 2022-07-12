import re

# 进行日期匹配
reg = "^(1[0-2]|[1-9])-(3[01]|[12][0-9]|[1-9])*:.*$"

s = '6-29:lwl'
ans = re.search(reg, s)

if ans != None:
    pattern2 = "\d+"
    date = re.findall(pattern2, s)
    to_user = s.split(':')[1]
    print(date, to_user)

print(ans)