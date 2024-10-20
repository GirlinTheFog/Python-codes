def Read():
  while(True):
    marks =[]
    for i in range(3):
      try:
        mark = int(input(f"Enter marks for Test {i+1}: "))
        if (mark > 0 & mark < 100):
          marks.append(mark)
        else:
          print("Invalid marks")
      except ValueError:
        print("Invalid input")
    return marks
marks = Read()
marks.sort()
print(marks)
avg = (marks[-1] + marks[-2])/2
print(avg)