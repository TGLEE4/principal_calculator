# --- Inform user about the restart option ---
print("Welcome to the Principal Calculator!")
print("Note: You can type 'restart' at any prompt to go back to the beginning.")
print("----------------------------------------------------------------------\n")

# --- Outer loop for restart functionality ---
while True:
    # Flag to check if a restart was requested
    restart_requested = False

    # --- Input for Principal Amount ---
    while True:
        print('What is the principal amount?')
        user_input = input() # Read input as string first
        if user_input.lower() == 'restart': # Check for restart
            restart_requested = True
            break # Exit inner loop
        try:
            principal = float(user_input)
            if principal <= 0:
                print("Principal amount must be greater than zero. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. No commas or special letters ($), only numbers and periods (.). For example: 34567.00")

    if restart_requested: # If restart was requested, skip to next iteration of outer loop
        continue

    # --- Input for Annual Interest Rate ---
    while True:
        print("What is the annual interest rate (as a percentage, e.g., 5, 5.4, or 5.4%)?")
        user_input = input() # Read input as string first
        if user_input.lower() == 'restart': # Check for restart
            restart_requested = True
            break # Exit inner loop
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
        continue

    # --- Input for Finance Agreement Duration and Unit ---
    time_value = 0.0 # Initialize outside the loop
    time_unit = ''   # Initialize outside the loop

    while True:
        print("What is your finance agreement duration?")
        user_input = input("Enter the number (e.g., 2, 2.5, 5): ") # Read input as string first
        if user_input.lower() == 'restart': # Check for restart
            restart_requested = True
            break # Exit inner loop
        try:
            time_value = float(user_input)
            if time_value <= 0:
                print("Duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 1, 2.5, 730).")

    if restart_requested:
        continue

    while True:
        print("Is that in (Y)ears, (M)onths, or (D)ays?")
        user_input = input("Enter Y, M, or D: ").strip().lower() # Check lower() for easier comparison
        if user_input == 'restart': # Check for restart
            restart_requested = True
            break # Exit inner loop

        if user_input in ['y', 'm', 'd']: # Compare with lowercased units
            time_unit = user_input.upper() # Store as uppercase for consistent logic
            break
        else:
            print("Invalid unit. Please enter Y for Years, M for Months, or D for Days.")

    if restart_requested:
        continue

    # --- Convert All Time Units to Years for Consistent Calculation ---
    time_years = 0.0
    if time_unit == 'M':
        time_years = time_value / 12  # Convert months to years
    elif time_unit == 'D':
        time_years = time_value / 365 # Convert days to years (approx)
    else: # time_unit == 'Y'
        time_years = time_value       # Already in years

    # --- Calculations ---
    rate_decimal = annual_rate / 100
    simple_interest = principal * rate_decimal * time_years
    total_amount = principal + simple_interest

    time_months = time_years * 12

    minimum_monthly_payment = 0.0
    if time_months > 0:
        minimum_monthly_payment = total_amount / time_months
    else:
        minimum_monthly_payment = 0.0

    # --- Displaying Results ---
    print("\n--- Calculation Results ---")
    print(f"Principal Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate}%")
    print(f"Original Time Input: {time_value:,.2f} {time_unit}")
    print(f"Total Time (Years): {time_years:,.2f}")
    print(f"Total Time (Months): {time_months:,.2f}")
    print(f"Calculated Simple Interest: ${simple_interest:,.2f}")
    print(f"Total Amount After Interest: ${total_amount:,.2f}")
    print(f"Estimated Minimum Monthly Payment: ${minimum_monthly_payment:,.2f}")
    print("---------------------------\n")

    # After displaying results, ask if the user wants to calculate again or exit
    while True:
        play_again = input("Calculate again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            print("\n----------------------------------------------------------------------")
            break # Breaks out of this inner loop, then outer loop continues for a new calculation
        elif play_again == 'no':
            print("Thank you for using the Simple Interest Calculator. Goodbye!")
            exit() # Exits the entire program
        elif play_again == 'restart': # User can type restart here too
            print("\n----------------------------------------------------------------------")
            restart_requested = True # Set flag to restart from the beginning
            break # Break from this inner loop to let outer loop handle restart
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if restart_requested: # If restart was requested after results, continue outer loop
        continue