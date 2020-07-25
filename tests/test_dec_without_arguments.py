from char import char
from char.main import ArgumentTypeError


def test_dec_without_arguments():
    """"""
    # Define function which will be checked via @char decorator
    @char
    def test_func_1(int_x, float_y, str_z):
        pass
    @char
    def test_func_2(list_x, dict_y, set_z):
        pass
    @char
    def test_func_3(is_y, has_y, bool_z):
        pass
    #####
    # Check that when types are correct no exceptions will be raised
    test_func_1(1, 1.0, "True")
    test_func_1(1, None, "True")
    test_func_2([], {}, {1,})
    test_func_2(None, {}, {1,})
    test_func_3(True, False, True)
    #####
    # Check that ArgumentTypeError Exception raised if something is wrong
    try:
        test_func_1(1, 1.0, 0)
    except ArgumentTypeError:
        pass
    else:
        raise Exception("Right Exception Was Not Raised")
    try:
        test_func_2([], {}, {})
    except ArgumentTypeError:
        pass
    else:
        raise Exception("Right Exception Was Not Raised")
    try:
        test_func_3(1, 0, 1)
    except ArgumentTypeError:
        pass
    else:
        raise Exception("Right Exception Was Not Raised")



