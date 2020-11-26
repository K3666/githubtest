def my_find_min_sample(sample_list):
    my_min = sample_list[0]    
    for item in sample_list:
        if item < my_min:
            my_min = item
    return my_min
