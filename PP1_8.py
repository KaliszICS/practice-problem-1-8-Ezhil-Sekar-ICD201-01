
def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)
def q2():
  #Write Assignment code here
  user = int(input( "Enter an integer: "))
  print(user !=0)
def q3():
  #Write Assignment code here
  user = float(input("Enter a number: "))
  print(user>=0 and user<=10)
def q4():
  #Write Assignment code here
  user = input("Input food: ")
  user2 = input("Input drink: ")
  print(not (user == 'pizza' and user2 == 'pop'))
def q5():
  #Write Assignment code here
  user = int(input("Enter an integer: "))
  print(f'The integer {user} is {user%2==0}')
#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''