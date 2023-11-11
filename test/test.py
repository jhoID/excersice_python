def is_paired(input_string):
    return True if input_string[0] == input_string[-1] else False
input_string = '[{}]'

print(is_paired(input_string))
