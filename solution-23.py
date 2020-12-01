def my_return_even_numbers(sample_list):
    even_numbers=[]
    for item in sample_list:
        if item % 2 == 0 :
            even_numbers.append(item)
    return even_numbers
