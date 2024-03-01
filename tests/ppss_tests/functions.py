from .variables import x_vals, y_vals, s_vals, sub_vals, vals_s1, vals_s2


def test_divide(divide, x_vals=x_vals, y_vals=y_vals):
    """
    Tests the divide function from HW3. It prints the value of x, y, and the result of the test.

    Args:
            x_vals (tuple): A tuple of numeric values. The defualt is x_vals from variables.
            y_vals (tuple): A tuple of numeric values. The defualt is y_vals from variables.
            divide (function): A function that returns the value of dividing x by y. If y equals to 0
            it return None.
    """
    for x in x_vals:
        for y in y_vals:
            result = divide(x=x, y=y)
            if y == 0 and result is None:
                val = "Ok"
            elif y != 0 and x / y == result:
                val = "Ok"
            else:
                val = "Bad"
            print(f"x = {x}, y = {y}: {val}")


def test_find_last(find_last, s_vals=s_vals, sub_vals=sub_vals):
    """
    Tests the find_last function from HW3. It prints the value of s, sub, and the result of the test.

    Args:
            s_vals (tuple): A tuple of non-empty strings. The defualt is s_vals from variables.
            sub_vals (tuple): A tuple of non-empty strings. The defualt is sub_vals from variables.
            find_last (function): A function that returns the index of the last occurance of sub in s.
            Returns None if sub does not occur in s.
    """
    for s in s_vals:
        for sub in sub_vals:
            result = find_last(s, sub)
            if result == s.rfind(sub):
                val = "Ok"
            elif result is None and s.rfind(sub) == -1:
                val = "Ok"
            else:
                val = "Bad"
            print(f"s = {s}, sub = {sub}: {val}")


def test_is_in(is_in, vals_s1=vals_s1, vals_s2=vals_s2):
    """
    Tests the is_in function from HW3. It prints the value of s1, s2, and the results of the test.

    Args:
            vals_s1 (tuple): A tuple of non-empty strings. The defualt is vals_s1 from variables.
            vals_s2 (tuple): A tuple of non-empty strings. The defualt is vals_s2 from variables.
            is_in (function): A function that returns True if either s1 or s2 occurs anywhere in the other,
            and False otherwise.
    """
    for s1 in vals_s1:
        for s2 in vals_s2:
            result = is_in(s1, s2)
            if (result and (s1.find(s2) != -1 or s2.find(s1) != -1)) or (
                not result and not (s1.find(s2) != -1 or s2.find(s1) != -1)
            ):
                val = "Ok"
            else:
                val = "Bad"
            print(f"s1 = {s1}, s2 = {s2}: {val}")
