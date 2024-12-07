def function_with_uncommon_error_solution(data):
    try:
        value = data['value']
        if isinstance(value,(int, float)) and value !=0:
          result = 1 / value
          return result
        elif isinstance(value,(int, float)) and value == 0:
          print("Error: Cannot divide by zero")
          return None
        else:
          print("Error: Invalid data type for division")
          return None

    except KeyError:
        print("Error: Key 'value' not found in the input data.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

my_data = {'value': 0}
result = function_with_uncommon_error_solution(my_data)
print(f"Result: {result}")

my_data = {'wrong_key': 1}
result = function_with_uncommon_error_solution(my_data)
print(f"Result: {result}")

my_data = {'value': 'abc'}
result = function_with_uncommon_error_solution(my_data)
print(f"Result: {result}")

my_data = {'value': 5}
result = function_with_uncommon_error_solution(my_data)
print(f"Result: {result}")
