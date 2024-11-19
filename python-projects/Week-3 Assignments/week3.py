# Create a function named calculate_discount(price, discount_percent) that calculates the final price after 
# applying a discount. The function should take the original price (price) and the discount percentage 
# (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, 
# return the original price.

def calculate_discount(price):
    discount_percent = 20  # Fixed discount of 20%
    if discount_percent >= 20:
        # Apply discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Get user input for the original price
try:
    original_price = float(input("Enter the original price: "))

    # Call the function and display the result
    final_price = calculate_discount(original_price)
    print(f"The final price after a 20% discount is: {final_price}")
except ValueError:
    print("Please enter a valid numerical value for the price.")


# # Question 2
# Using the calculate_discount function, prompt the user to enter the original price of an item and
# the discount percentage. Print the final price after applying the discount, or if no discount was 
# applied, print the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Get user input for the original price and discount percentage
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function and display the result
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price != original_price:
        print(f"The final price after a {discount_percent}% discount is: {final_price}")
    else:
        print(f"No discount applied. The original price is: {original_price}")
except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")
