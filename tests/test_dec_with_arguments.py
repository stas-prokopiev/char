from char import char
from char.main import ArgumentTypeError


def test_dec_with_arguments():
    """"""
    # Define function which will be checked via @char decorator
    dict_tuple_types_by_prefix = {"hihi_": (int), "wow": (bool)}
    @char(dict_tuple_types_by_prefix=dict_tuple_types_by_prefix)
    def test_func_1(hihi_x, wowy):
        pass
    dict_tuple_types_by_prefix_to_update_default = {"wow2": (str)}
    @char(dict_tuple_types_by_prefix_to_update_default=\
        dict_tuple_types_by_prefix_to_update_default)
    def test_func_2(list_x, dict_y, set_z, wow2):
        pass
    @char(bool_is_to_skip_None_value=False)
    def test_func_3(is_y, has_y, bool_z):
        pass
    #####
    # Check that when types are correct no exceptions will be raised
    test_func_1(1, True)
    test_func_2([], {}, {1,}, "string")
    test_func_3(True, False, True)
    # #####
    # Check that ArgumentTypeError Exception raised if something is wrong
    try:
        test_func_1(1, 0)
    except ArgumentTypeError:
        pass
    else:
        raise Exception("Right Exception Was Not Raised")
    try:
        test_func_2([], {}, {1,}, [])
    except ArgumentTypeError:
        pass
    else:
        raise Exception("Right Exception Was Not Raised")
    try:
        test_func_3(None, False, True)
    except ArgumentTypeError:
        pass
    else:
        raise Exception("Right Exception Was Not Raised")



