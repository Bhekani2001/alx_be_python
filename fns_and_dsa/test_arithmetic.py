from arithmetic_operations import perform_operation

def test():
    print(perform_operation(5, 6, 'add'))        # Expected: 11
    print(perform_operation(10, 4, 'subtract'))  # Expected: 6
    print(perform_operation(3, 7, 'multiply'))   # Expected: 21
    print(perform_operation(8, 2, 'divide'))     # Expected: 4.0
    print(perform_operation(8, 0, 'divide'))     # Expected: Error: Division by zero
    print(perform_operation(8, 2, 'modulus'))    # Expected: Error: Invalid operation

if __name__ == "__main__":
    test()
