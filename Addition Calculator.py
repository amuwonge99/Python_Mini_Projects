import sys

total: float=0
while True:
    user_input: str = input ('Enter a number: ')
    
    if user_input == '0':
        print(f'Total: {total}')
        sys.exit()
        
    try:
        total+= float(user_input)
    except ValueError:
        print('Please enter a valid number')