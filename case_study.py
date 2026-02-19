item1=float(input("Enter the price of item 1:"))
item2=float(input("Enter the price of item 2:"))
item3=float(input("Enter the price of item 3:"))
total_cost=item1+item2+item3
discount = 0
if total_cost > 50:
    discount = 0.10 * total_cost
final_cost = total_cost - discount
print("\n---Billing Details---")
print(f"Total Cost:${total_cost:.2f}")
print(f"Discount:${discount:.2f}")
print(f"Final Cost:${final_cost:.2f}")
