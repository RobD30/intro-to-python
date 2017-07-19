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


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function

    return sorted(input_list[-3:0])
