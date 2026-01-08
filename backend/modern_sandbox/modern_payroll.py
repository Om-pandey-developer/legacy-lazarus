import sys

def calculate_pay():
    """
    Calculates total pay based on hours worked and hourly rate,
    applying overtime rules (1.5x > 40h) and a hidden bonus (+50 if total > 1000).
    """
    try:
        # 1. Input Parsing from sys.argv
        # Assuming inputs are provided as command-line arguments
        hours = float(sys.argv[1])
        rate = float(sys.argv[2])
    except (IndexError, ValueError):
        # Graceful exit if arguments are missing or invalid, though environment implies valid inputs
        return

    BASE_HOURS = 40.0
    OT_MULTIPLIER = 1.5
    BONUS_THRESHOLD = 1000.0
    BONUS_AMOUNT = 50.0

    subtotal_pay = 0.0

    # 2. Logic: Calculate Pay (including Overtime)
    if hours <= BASE_HOURS:
        subtotal_pay = hours * rate
    else:
        # Base Pay
        base_pay = BASE_HOURS * rate
        
        # Overtime Pay
        ot_hours = hours - BASE_HOURS
        ot_pay = ot_hours * rate * OT_MULTIPLIER
        
        subtotal_pay = base_pay + ot_pay

    # 3. Logic: Apply Hidden Bonus
    final_pay = subtotal_pay
    if subtotal_pay > BONUS_THRESHOLD:
        final_pay += BONUS_AMOUNT

    # 4. CRITICAL: Cast result to int() and Print ONLY the result
    print(int(final_pay))

if __name__ == "__main__":
    calculate_pay()