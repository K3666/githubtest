def my_return_even_numbers(sample_list):
    # Create an empty list
    even_numbers=[]
    # Iterate through the input list
    for item in sample_list:
        # determine if an element is even
        if item % 2 == 0 :
            even_numbers.append(item)
    # finally return the list of even numbers
    return even_numbers
