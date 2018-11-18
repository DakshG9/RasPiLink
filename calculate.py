# Sum numbers 
def sum_numbers(*tuple_numbers):
    length_tuple = len(tuple_numbers)
    answer = 0 
    for tuple_counter in range(0,length_tuple):
       answer = answer + tuple_numbers[tuple_counter]

    return(answer)

#substract numbers
def substract_numbers(*tup_num):
    length_tup = len(tup_num)
    answer = 0
    tup_counter = 0
    while tup_counter != length_tup:
        answer = answer - tup_num[tup_counter]
        tup_counter = tup_counter + 1
    return(answer)

#multiply
def multiply_numbers(*tup_num):
    length_tup = len(tup_num)
    answer = 1
    tup_counter = 0
    while tup_counter != length_tup:
        answer = answer * tup_num[tup_counter]
        tup_counter = tup_counter + 1
    return(answer)


#divide
def divide_numbers(*tuple_numbers):
    length_tuple = len(tuple_numbers)
    answer =  tuple_numbers[0]
    for tuple_counter in range(1,length_tuple):
       answer = answer / tuple_numbers[tuple_counter]

    return(answer)
def square_power(num_to_square, *power):
    if len(power) == 0:
        answer = num_to_square ** 2
    else:
        answer = num_to_square ** power(0)




