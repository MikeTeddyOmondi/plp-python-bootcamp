def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
    
    Returns:
        float: The final price after applying the discount if it is 20% or higher;
               otherwise, returns the original price.
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the result
    if final_price < original_price:
        print(f"Discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Please enter a valid number for the price and discount percentage.")
