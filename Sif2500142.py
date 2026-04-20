print ("Enter Student Name:")
name = input("")

print ("Enter The Total classes held:")
classes = float(input(""))

print ("Enter The Total Classes You Attend:")
attend_classes = float(input(""))

print ("Enter Student's Course")
course = input("")

a_persentage = ((attend_classes/classes)*100)
print("attendance percentage",a_persentage)

clp = a_persentage

if clp >= 75:
  print("Allowed for exam")
else:
  print("Not allowed for exam")
