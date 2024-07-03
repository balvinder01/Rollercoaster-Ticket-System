print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
  print("You can ride the Rollercoaster")
  age = int(input("What is your age?\n"))
  if age < 12:
    bill = 5
    print("Child ticket are $5")
  elif age <= 18:
    bill = 7
    print("Youth ticket are $7")
  elif age>=45 and age<=55:
    print("Everything is going to be ok. Have a free ride on us.")
  else:
    bill = 12
    print("Adult ticket are $12")
  want_photo = input("do you want to photo taken? Y or N.")
  if want_photo == "Y":
    bill += 3
    print(f"Your total bill is ${bill}")
  else:
    bill += 0
    print(f"Your final bill is ${bill}")
else:
  print("sorry,you have to grow taller before you can ride")
