import os # Import the 'os' module for operating system interactions
import time # Import 'time' for a small delay before clearing

# --- Function to clear the screen based on OS ---
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (posix)
    else:
        _ = os.system('clear')

# --- Inform user about the restart option ---
print("Welcome to the principal Interest Calculator!")
print("Note: You can type 'restart' at any prompt to go back to the beginning.")
print("----------------------------------------------------------------------\n")

# --- Outer loop for restart functionality ---
while True:
    restart_requested = False
    
    # Clear screen at the beginning of a new calculation round
    # We'll skip clearing immediately after the welcome message to let it be seen.
    # clear_screen() # You could uncomment this if you want to clear right after welcome.

    # --- Input for Principal Amount ---
    while True:
        print('What is the principal amount?')
        user_input = input()
        if user_input.lower() == 'restart':
            restart_requested = True
            break
        try:
            principal = float(user_input)
            if principal <= 0:
                print("Principal amount must be greater than zero. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. No commas or special letters ($), only numbers and periods (.). For example: 34567.00")

    if restart_requested:
        clear_screen() # Clear screen before restarting
        continue

    # --- Input for Annual Interest Rate ---
    while True:
        print("What is the annual interest rate (as a percentage, e.g., 5, 5.4, or 5.4%)?")
        user_input = input()
        if user_input.lower() == 'restart':
            restart_requested = True
            break
        try:
            annual_rate_input = user_input

            if annual_rate_input.endswith('%'):
                annual_rate_input = annual_rate_input[:-1]

            annual_rate = float(annual_rate_input)

            if annual_rate < 0:
                print("Interest rate cannot be negative. Please enter a positive number.")
                continue

            break
        except ValueError:
            print("Invalid input. Please enter a number, optionally followed by a '%' (e.g., 5, 5.4, 5.4%).")

    if restart_requested:
        clear_screen() # Clear screen before restarting
        continue

    # --- Input for Finance Agreement Duration and Unit ---
    time_value = 0.0
    time_unit = ''

    while True:
        print("What is your finance agreement duration?")
        user_input = input("Enter the number (e.g., 2, 2.5, 730): ")
        if user_input.lower() == 'restart':
            restart_requested = True
            break
        try:
            time_value = float(user_input)
            if time_value <= 0:
                print("Duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 1, 2.5, 730).")

    if restart_requested:
        clear_screen() # Clear screen before restarting
        continue

    while True:
        print("Is that in (Y)ears, (M)onths, or (D)ays?")
        user_input = input("Enter Y, M, or D: ").strip().lower()
        if user_input == 'restart':
            restart_requested = True
            break

        if user_input in ['y', 'm', 'd']:
            time_unit = user_input.upper()
            break
        else:
            print("Invalid unit. Please enter Y for Years, M for Months, or D for Days.")

    if restart_requested:
        clear_screen() # Clear screen before restarting
        continue

    # --- Convert All Time Units to Years for Consistent Calculation ---
    time_years = 0.0
    if time_unit == 'M':
        time_years = time_value / 12
    elif time_unit == 'D':
        time_years = time_value / 365
    else: # time_unit == 'Y'
        time_years = time_value

    # --- Calculations ---
    rate_decimal = annual_rate / 100
    principal_interest = principal * rate_decimal * time_years
    total_amount = principal + principal_interest

    time_months = time_years * 12

    minimum_monthly_payment = 0.0
    if time_months > 0:
        minimum_monthly_payment = total_amount / time_months
    else:
        minimum_monthly_payment = 0.0

    # --- Displaying Results ---
    # Clear screen before showing results for a clean display
    clear_screen()
    print("\n--- Calculation Results ---")
    print(f"Principal Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate}%")
    print(f"Original Time Input: {time_value:,.2f} {time_unit}")
    print(f"Total Time (Years): {time_years:,.2f}")
    print(f"Total Time (Months): {time_months:,.2f}")
    print(f"Calculated principal Interest: ${principal_interest:,.2f}")
    print(f"Total Amount After Interest: ${total_amount:,.2f}")
    print(f"Estimated Minimum Monthly Payment: ${minimum_monthly_payment:,.2f}")
    print("---------------------------\n")

    # After displaying results, ask if the user wants to calculate again or exit
    while True:
        play_again = input("Calculate again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            print("\nStarting a new calculation...\n")
            time.sleep(1) # Small delay for the user to read the message
            clear_screen() # Clear screen before restarting for a clean slate
            break
        elif play_again == 'no':
            print("Thank you for using the principal Interest Calculator. Goodbye!")
            exit()
        elif play_again == 'restart': # User can type restart here too
            print("\nRestarting from the beginning...\n")
            time.sleep(1) # Small delay
            restart_requested = True
            clear_screen() # Clear screen immediately
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if restart_requested:
        continue # This will go back to the outermost while True loop
