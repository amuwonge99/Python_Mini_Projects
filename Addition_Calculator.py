print()
print("I'm a genius. Give me as many numbers as you want, and I'll add them up for you.")
print("When you're done, just type 'exit' to see the total.")
print()

import sys

total: float = 0
while True:
    user_input: str = input('Enter a number (or type "exit" to quit): ')
    
    if user_input.lower() == 'exit':
        print(f'Total: {total}')
        sys.exit()
        
    try:
        total += float(user_input)
    except ValueError:
        print('Please enter a valid number')
