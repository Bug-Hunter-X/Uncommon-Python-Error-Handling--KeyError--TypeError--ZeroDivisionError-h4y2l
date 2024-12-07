def function_with_uncommon_error(data):
    try:
        result = 1 / data['value']  # Potential ZeroDivisionError
        return result
    except KeyError:
        return 0
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return None

my_data = {'value': 0}
result = function_with_uncommon_error(my_data)
print(f"Result: {result}")

my_data = {'wrong_key': 1}
result = function_with_uncommon_error(my_data)
print(f"Result: {result}")

my_data = {'value': 'abc'}
result = function_with_uncommon_error(my_data)
print(f"Result: {result}")