def build_shift_dict(self, shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    # create a new list of letters based on the shift
    shifted_lowercase = list(string.ascii_lowercase[shift:]) + list(string.ascii_lowercase[:shift])
    shifted_uppercase = list(string.ascii_uppercase[shift:]) + list(string.ascii_uppercase[:shift])

    # empty dict
    d = {}

    # populate dict for lowercase
    for l in range(len(string.ascii_lowercase)):
        d[string.ascii_lowercase[l]] = shifted_lowercase[l]

    # populate dict for uppercase
    for l in range(len(string.ascii_uppercase)):
        d[string.ascii_uppercase[l]] = shifted_uppercase[l]

    return d