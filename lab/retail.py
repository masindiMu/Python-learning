def main():

    description = get_retail_item_description()
    items_bought =  get_number_of_purchased_items()
    price_usd = get_price_usd_per_unit()
    tax_rate = get_tax_rate()

    subtotal = calculate_subtotal_usd(price_usd, items_bought)
    tax = calculate_tax_usd(subtotal, tax_rate)
    total = calculate_total_usd(subtotal, tax)

    print(f"\nDescription: {description}")
    print(f"Quantity Sold: {items_bought}")
    print(f"Price per Unit: ${price_usd:.2f}")
    print(f"Subtotal: ${subtotal:}")
    print(f"Tax: ${tax:}")
    print(f"Total: ${total:}")



def get_retail_item_description():
    """
    
    :return:
    """
    description = input("What is the retail item description?")
    return description


def get_number_of_purchased_items():
    items_bought= int ( input("Enter items purchased:"))
    return int(items_bought)


def get_price_usd_per_unit():
    price_usd = float(input("Enter price per unit(usd):"))
    return float(price_usd)

def get_tax_rate():
    tax_rate = float( input("Enter tax rate, (e.g. 0.06 for 6%):"))
    return float(tax_rate)

def calculate_subtotal_usd(price_usd, items_bought):
    subtotal = float(price_usd * items_bought)
    return float(subtotal)


def calculate_tax_usd(subtotal, tax_rate):
    tax_usd = (subtotal * tax_rate)
    return tax_usd


def calculate_total_usd(subtotal_usd, tax_rate):
    total = subtotal_usd + tax_rate
    return total

if __name__ == "__main__":
    main()
