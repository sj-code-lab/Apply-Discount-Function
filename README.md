# Apply Discount Function — freeCodeCamp Lab

## 📌 What I Did
I completed the **“Build an Apply Discount Function”** lab on freeCodeCamp.  
The goal was to write a Python function named `apply_discount` that calculates the final price of an item after applying a percentage discount. The function also needed to validate inputs and return specific error messages when invalid values were provided.

---

## ✅ Tests That Had to Be Passed
To complete the lab, the function had to satisfy all user stories and pass the following tests:

1. The function must be named **apply_discount**.
2. It must accept exactly **two parameters**: `price` and `discount`.
3. If `price` is not an `int` or `float`, return:  
   **"The price should be a number"**
4. If `discount` is not an `int` or `float`, return:  
   **"The discount should be a number"**
5. If `price` is less than or equal to 0, return:  
   **"The price should be greater than 0"**
6. If `discount` is less than 0 or greater than 100, return:  
   **"The discount should be between 0 and 100"**
7. Correctly compute the final price for valid inputs:
   - `apply_discount(100, 20)` → `80`
   - `apply_discount(200, 50)` → `100`
   - `apply_discount(50, 0)` → `50`
   - `apply_discount(100, 100)` → `0`
   - `apply_discount(74.5, 20.0)` → `59.6`

All tests were successfully passed.
---

## 🧠 My Solution
```python
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
