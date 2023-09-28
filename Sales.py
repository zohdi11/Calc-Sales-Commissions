def calculate_commission(product, sales_amount):
    # Define commission rates and sales tiers for each product
    if product == 'Product A':
        if 10000 <= sales_amount < 20000:
            commission_rate = 0.05
        elif 20000 <= sales_amount < 40000:
            commission_rate = 0.075
        elif sales_amount >= 40000:
            commission_rate = 0.09
        else:
            return None
    elif product == 'Product B':
        if 15000 <= sales_amount < 25000:
            commission_rate = 0.06
        elif 25000 <= sales_amount < 40000:
            commission_rate = 0.08
        elif sales_amount >= 40000:
            commission_rate = 0.1
        else:
            return None
    elif product == 'Product C':
        if 12000 <= sales_amount < 22000:
            commission_rate = 0.03
        elif 22000 <= sales_amount < 40000:
            commission_rate = 0.045
        elif sales_amount >= 40000:
            commission_rate = 0.055
        else:
            return None
    else:
        return None
    
    commission = sales_amount * commission_rate
    return commission

def main():
    print("Welcome to the Sales Commission Calculator!")

    # Get user input for product and sales amount
    product = input("Enter the product (Product A, Product B, or Product C): ")
    sales_amount = float(input("Enter the sales amount: "))

    # Calculate commission
    commission = calculate_commission(product, sales_amount)

    if commission is not None:
        print(f"The commission for selling {product} worth ${sales_amount} is ${commission:.2f}")
    else:
        print("Invalid product. Please enter Product A, Product B, or Product C.")

if __name__ == "__main__":
    main()
