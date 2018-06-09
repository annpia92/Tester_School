mport correct_date
def validate(x):
    if correct_date.not_empty(x)==False:
        return False
    if correct_date.length_pesel(x)==False:
        return False
    if correct_date.is_positiveNumber(x) == False:
        return False
    if correct_date.val_checksum(x)==False:
        return False
    if correct_date.correctDate(x)==False:
        return False

return True