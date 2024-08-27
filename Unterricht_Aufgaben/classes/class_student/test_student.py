from class_student  import Student

           
person1 = Student("Susi", "weiblich", 22, "Fachrichtung Technik")
#print(person1.vorname, person1.alter)

person2 = Student("Benno", "männlich", 24, "Fachrichtung Management")
#print(person2.vorname, person2.alter)

person1.hat_geburtstag()
#print(person1.vorname)
person2.hat_geburtstag()
person2.weckselt_fachrichtung("Technik")

# print(person2.vorname)
# print(person1.vorname)
print(person2.fachrichtung)
print(person1.get_alter())

print(person1)
print(person2)