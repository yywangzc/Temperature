driving = input('Have you ever driven a car? : ')
if driving != 'Yes' and driving != 'No':
	print('Please key in Yes/No')
	raise SystemExit

age = input('What is your age? : ')
age = int(age)
if driving == 'Yes':
	if age >= 18:
	    print('Pass')
	else:
		print('Without a license')
elif driving == 'No':
    if age >= 18:
    	print('Can test drivers license')
    else:
    	print('Can test drivers license soon')
else:
    print('Please key in Yes/No')    