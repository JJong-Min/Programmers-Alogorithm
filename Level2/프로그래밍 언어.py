table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
new_table=[]
answer = []
points = []
for i in range(len(table)):
  new_table.append(list(table[i].split()))
for job in new_table:
  point = 0
  j = 0
  for language in languages:
    if language not in job:
      j+=1
      continue
    point += (6-job.index(language)) * preference[j]
    j += 1
  points.append(point)
  job.append(point)

max_point = max(points)
for row in new_table:
  if max_point == row[6]:
    answer.append(row[0])

answer.sort()
print(answer[0])


