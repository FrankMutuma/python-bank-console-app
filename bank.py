import os

#method create account
def createaccount():
	name=input("Enter your name: ")
	id_no=input("Enter your id number: ")
	import random
	accno=random.randint(1000000,99999999)
	users[accno]={"Name":name,"Idnumber":id_no, "DepositAmount":0.0,"LoanAmount":0.0}
	print(f"Hello {name} your Account Number is: {accno}")
	input("Press any Enter key to continue...")
	os.system('clear')
	
#method Login
def login():
		search_str=input("Enter your (Account or Id) number to login:  ")
		#print(accounts)
		user_accno = next((accno for accno,details in users.items() if details.get("Idnumber") == search_str),search_str if search_str in users else None)
		if user_accno:
			os.system("clear")
			account(user_accno)
		else:
			input(f"{search_str} not found...press any key to continue..")
			os.system("clear")
			
			
#method deposit
def deposit(acc_no):
	amount=input(f"welcome {users[acc_no]['Name']}\n Your account balance is : ksh {users[acc_no]['DepositAmount']}\n Enter the amount to Deposit: ")
	users[acc_no]['DepositAmount']=str(float(users[acc_no]['DepositAmount'])+float(amount))
	print(f"Deposit of Ksh. {amount} succesfull your account balance is Ksh. {users[acc_no]['DepositAmount']}\n")
	input("Press any Enter key to continue...")
	os.system('clear')
	account(acc_no)
	
#method withdraw
def withdraw(acc_no):
	amount=float(input(f"welcome {users[acc_no]['Name']}\n Your account balance is : ksh {users[acc_no]['DepositAmount']}\n Enter the amount to Withdraw: "))
	if amount<float(users[acc_no]['DepositAmount'])+2.0 :
		users[acc_no]['DepositAmount']=str(float(users[acc_no]['DepositAmount'])-amount-2)
		print(f"Withdrawal of Ksh. {amount} succesfull your account balance is Ksh. {users[acc_no]['DepositAmount']}, transaction cost Ksh. 2.00\n")
		input("Press any key to continue...")
	else:
		print("Insufficient balance to withdraw ksh. {amount}, kindly topup, \nyou can borrow with us today to purchase without interuptions.")
	os.system('clear')
	account(acc_no)
	
#repay method
def repay(acc_no):
	amount=float(input(f"\nYour outstanding loan balance is : ksh {users[acc_no]['LoanAmount']}\n Enter the amount to repay: "))
	if amount>float(users[acc_no]['LoanAmount']) :
		amount=float(users[acc_no]['LoanAmount'])
	if amount>float(users[acc_no]['DepositAmount']):
		print(f"\n\nInsufficient balance to Repay ksh. {amount}, kindly topup yo enjoy our services\n")
		input("\nPress any Enter key to continue...")
		os.system('clear')
		account(acc_no)
	users[acc_no]['DepositAmount']=str(float(users[acc_no]['DepositAmount'])-amount)
	users[acc_no]['LoanAmount']=str(float(users[acc_no]['LoanAmount'])-amount)
	print(f"\n\nYour loan repayment request of Ksh. {amount} is succesfull. your loan balance is Ksh. {users[acc_no]['LoanAmount']}, transaction cost Ksh. 0.00\n")
	input("\nPress any Enter key to continue...")
	os.system('clear')
	account(acc_no)

#method borrow
def borrow(acc_no):
	print("borrow")
	if 5000-float(users[acc_no]['LoanAmount'])<=0:
					choice=input("\n\nkindly repay your current loan to be able to borrow\nPress 1 to repay any or any other key to continue...")
					if choice=="1":
						os.system("clear")
						repay(acc_no)
					else:
						return
	amount=float(input("\nEnter the amount to Borrow: "))
	while amount>5000-float(users[acc_no]['LoanAmount']): amount=float(input("\nThe amount entered exceeds your limit kindly enter a lower amount: "))
	if amount<=5000.0-float(users[acc_no]['LoanAmount']):
					users[acc_no]['LoanAmount']=str(float(users[acc_no]['LoanAmount'])+(amount *116/100))
					users[acc_no]['DepositAmount']=str(float(users[acc_no]['DepositAmount'])+amount)
					print(f"\n\nLoan request of Ksh. {amount} succesfull your account balance is Ksh. {users[acc_no]['DepositAmount']},\n a loan of ksh. {users[acc_no]['LoanAmount']} is due in 2 weeks. transaction cost Ksh. 0.00\n\n")

	input("Press any Enter key to continue...")
	os.system("clear")	
	account(acc_no)
	


#method loans
def loans(acc_no):
		choice=input(f"\n You have a loan of Ksh. {users[acc_no]['LoanAmount']}\nyour remaining loan limit is : ksh {5000-float(users[acc_no]['LoanAmount'])}\n All loans are charged 16 %interest\n press\n 1. to borrow. \n 2. to repay: ")
		if choice=='1':
			borrow(acc_no)
		elif choice=='2':
			repay(acc_no)
		else:
			os.system("clear")
			account(acc_no)
			
			
#method loggedin account
def account(acc_no):
	choice=input(f"welcome {users[acc_no]['Name']}\n Your account balance is : ksh {users[acc_no]['DepositAmount']}\n 1. Deposit funds \n 2. Withdraw funds\n 3. Loans\n")
	if choice=="1":
		os.system('clear')
		deposit(acc_no)
	elif choice=="2":
		os.system('clear')
		withdraw(acc_no)
	else:
		loans(acc_no)
		#break

#method main
users={}
users["Test"]={"Name":"admin","Idnumber":"1234", "DepositAmount":1500,"LoanAmount":4000}
print(users)
while True:
	print("Hello welcome to YourBank")
	choice=input("1. Create account\n2. login\n")
	if choice=="1":
		os.system('clear')
		print("Welcome lets create your account")
		createaccount()
	elif choice=="2":
		os.system('clear')
		print("Welcome lets login")
		login()
	else:
		break