import random
import sys

for i in range(5):  # This runs the code 5 times
    print(f"--- Run {i+1} ---")
    sys.stdout.flush()  # Force output to display immediately
    
    # adds numbers
    add1 = random.randint(1,10)
    add2 = random.randint(0,10)
    # multiplies numbers
    mul1 = random.randint(1,10)
    mul2 = random.randint(1,10)
    
    # if 2nd value greater than zero adds and if not multiplies
    if add2 > 0:
        print("doing addition")
        add = add1 + add2
        #prints the result of addition
        print(f"Result: {add}")
    else:
        print("doing multiplication")
        mul = mul1 * mul2
        #prints the result of multiplication
        print(f"Result: {mul}")
    
    print()  # Add blank line between runs
    sys.stdout.flush()  # Force output to display immediately

print("All 5 runs completed!")
sys.stdout.flush()
