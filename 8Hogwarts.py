students = [
   {"name": "Harry", "house": "Gryf", "Patronus": "Otter"},
   {"name": "Biba", "house": "Les", "Patronus": "BobrKurva"},
   {"name": "Biba", "house": "Chawa", "Patronus": "Dogi"}
]

for student in students:
   print(student["Patronus"], student["house"], student["name"], sep="-")