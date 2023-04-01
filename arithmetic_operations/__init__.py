# Ajusta o valor a ser o divisor em caso de número 0
def check_value_den(value):
    if value <= 0:
        return 1
    else:
        return value
