User_PT = input("Enter your patient's PT in seconds: ")
User_PT = float(User_PT)
User_Normal = input("Enter the normal PT value. If you don't have one just type 0 and our standard of 11.5s will be used")
User_Normal = float(User_Normal)
if User_Normal <= 6 or User_Normal >= 18: #Crude way of using program's own PT normal
	User_Normal = 11.5
	print("Program's own PT normal is being used. It was requested or your value was implausible. ") #Remove this if you don't want the clutter. Its there in case people enter their value wrong
User_ISI =  input("Enter the ISI of your reagent")
User_ISI = float(User_ISI)
INR = ((User_PT/User_Normal)**User_ISI)
INR = round(INR,2)
INR = str(INR)
print("Your INR is: " + INR)
#The commented out lines are just providing some clinical explanations for the numbers for students who might not know about INR not for clinical use. Comments and intervals are debatable.
'''
if float(INR) > 4.5 and float(INR) < 5:
	print("An INR > 4.5 indicates a high risk of bleeding.")
elif float(INR) >= 2.0 and float(INR)<= 3.0:
	print("An INR between 2.0-3.0 is often targeted for patients taking warfarin.")
elif float(INR) >= 5:
	print("An INR > 5.0 is critical and should require attention.")
elif float(INR) >= 0.8 and float(INR) <= 1.2:
	print("INR is considered to be within normal range for your average patient.")
'''
