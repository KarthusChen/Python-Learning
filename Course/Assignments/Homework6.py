import math

def fee(hours):
    # Base charge for up to 3 hours
    base_charge = 20.0
    # Additional charge per hour after 3 hours
    additional_rate = 5.0
    # Maximum charge for any 24-hour period
    max_charge = 50.0

    # If the car was parked for 3 hours or less
    if hours <= 3:
        return base_charge
    else:
        # Calculate the additional hours, round them up, and compute the additional fee
        additional_hours = math.ceil(hours - 3)
        additional_fee = additional_hours * additional_rate
        # Total fee is the sum of the base charge and the additional fee, capped at the maximum charge
        return min(base_charge + additional_fee, max_charge)

# Example usage:
print(fee(2))  # Output: 20.0
print(fee(3))  # Output: 20.0
print(fee(3.1)) # Output: 25.0
print(fee(7.2)) # Output: 45.0
print(fee(8.2)) # Output: 50.0
print(fee(24))  # Output: 50.0
