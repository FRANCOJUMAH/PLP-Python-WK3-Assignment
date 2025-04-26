def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.
    
    Returns:
    - float: The final price after the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Output the result
    if final_price < original_price:
        print(f"A discount of {discount_percentage}% has been applied.")
        print(f"The final price is: ${final_price:.2f}")
    else:
        print("No discount applied.")
        print(f"The original price is: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")