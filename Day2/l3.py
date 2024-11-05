# Removing elements
vegetables = ["carrot", "broccoli", "lettuce", "tomato", "spinach"]

vegetables.remove("tomato")    
removed_vegetable = vegetables.pop(2) 

vegetables.clear()

print("Removed vegetable:", removed_vegetable)
print("Vegetables after clear:", vegetables)
