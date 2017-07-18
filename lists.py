def foo():
    order = [1, 2, 3, 4, 5, 6, 7, 8]
    return order


dish = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
mr_buns_order = dish
print(dish)
print(mr_buns_order)
dish[6] = "Spam"  # baked beans are off
print(mr_buns_order)
print(dish)
