# Tuple with items and total cost
items = (
    ("apple", 0.5, 4),    
    ("banana", 0.3, 6),
    ("orange", 0.8, 3)
)

total_cost = sum(price * quantity for _, price, quantity in items)

print("Items:", items)
print("Total cost:", total_cost)
