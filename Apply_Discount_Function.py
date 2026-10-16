# Function to apply discount
def apply_discount(price, discount):
    # Validate that price is a number (int or float)
    if not isinstance(price, int) and not isinstance(price, float):
        return 'The price should be a number'
    
    # Validate that discount is a number (int or float)
    if not isinstance(discount, int) and not isinstance(discount, float):
        return 'The discount should be a number'
    
    # Price must be positive to make sense in a discount calculation
    if price <= 0:
        return 'The price should be greater than 0'
    
    # Discount must be within a realistic percentage range
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    
    # Calculate the discount amount (percentage of the price)
    discount_amount = price * (discount / 100)
    
    # Subtract the discount from the original price
    final_price = price - discount_amount
    
    # Return the final price after discount
    return final_price
