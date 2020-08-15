"""
This is one and only file with working code in the whole package
"""

# Standard library imports
import sys
import logging
from functools import wraps
# Third party imports

# Local imports


LOGGER = logging.getLogger("check_types_of_arguments")
LOGGER.addHandler(logging.NullHandler())


DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX = {}
#####
# First define prefixes which are python version specific
if sys.version_info[0] == 2:
    # basestring is parent class for str and unicode
    DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["str_"] = (basestring)
else:
    DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["str_"] = (str)
#####
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["any_"] = (object)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["bytes_"] = (bytes)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["bool_"] = (bool)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["b_"] = (bool)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["is_"] = (bool)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["has_"] = (bool)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["int_"] = (int)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["i_"] = (int)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["float_"] = (float)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["f_"] = (float)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["list_"] = (list)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["l_"] = (list)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["dict_"] = (dict)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["d_"] = (dict)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["set_"] = (set)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["s_"] = (set)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["tuple_"] = (tuple)
DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX["t_"] = (tuple)



class ArgumentTypeError(TypeError):
    """Error that type of argument is incorrect

    Args:
        TypeError (Exception): Wrong type of argument was given to function
    """
    pass


def check_type_of_1_argument(
        str_function_name,
        str_argument_name,
        argument_value,
        tuple_types_var_can_be
):
    """Check type of one argument for function

    Args:
        str_function_name (str): Name of function from which method is called
        str_argument_name (str): Name of argument to check
        argument_value (Any): Value that was given to this argument
        tuple_types_var_can_be (tuple of types): Types this arg can be

    Raises:
        ArgumentTypeError: Wrong type of argument, child from TypeError
    """
    if isinstance(argument_value, tuple_types_var_can_be):
        return
    str_error_message = (
        "Incorrect type of variable was given to function: " +
        str_function_name + "\n" +
        "---> For variable: " + str(str_argument_name) + "\n" +
        "---> Were given value: " + str(argument_value) + "\n" +
        "---> With type: " + str(type(argument_value)) + "\n" +
        "---> Instead of: " + str(tuple_types_var_can_be)
    )
    raise ArgumentTypeError(str_error_message)


def char(
        function=None,
        dict_tuple_types_by_prefix=None,
        dict_tuple_types_by_prefix_to_update_default=None,
        bool_is_to_skip_none_value=True,
):
    """Decorator for checking types of arguments in function

    Check is done according to prefices that was given (or default ones)
    E.G.
        if name of variable starts with int_ and
        there is prefix "int_" in dict which describe how to check types
        then if for the argument will be given value with any another type
        then ArgumentTypeError Exception will be raised

    Args:
        function (function, optional):
            To call dec without arguments. Defaults to None.
        dict_tuple_types_by_prefix (dict, optional):
            Rules how to check types. Defaults to None.
        dict_tuple_types_by_prefix_to_update_default (dict, optional):
            Additional to default Rules how to check types. Defaults to None.
        bool_is_to_skip_none_value (bool, optional):
            Flag what to do with None values. Defaults to True.

    Returns:
        function: Decorator without arguments
    """
    # Process additional arguments
    if dict_tuple_types_by_prefix is None:
        dict_tuple_types_by_prefix_local = DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX
    else:
        dict_tuple_types_by_prefix_local = dict_tuple_types_by_prefix
    if dict_tuple_types_by_prefix_to_update_default is not None:
        dict_tuple_types_by_prefix_local.update(
            dict_tuple_types_by_prefix_to_update_default)


    def cfa_with_args(func_to_check):
        """Main decorator without arguments

        Args:
            func_to_check (function): decorated function

        Returns:
            function: Decorated function
        """
        int_args_count = func_to_check.__code__.co_argcount
        list_function_arguments = \
            func_to_check.__code__.co_varnames[:int_args_count]
        str_function_name = func_to_check.__name__
        @wraps(func_to_check)
        def wrapper(*args, **kwargs):
            """wrapper for decorated function

            Returns:
                Any: Result of the decorated function
            """
            dict_local_variables = locals()
            tuple_args = dict_local_variables['args']
            dict_kwargs = dict_local_variables['kwargs']
            list_tuples_to_iterate = (
                list(zip(list_function_arguments, tuple_args)) +
                list(dict_kwargs.items())
            )
            #####
            # Check arguments one by one
            for str_argument_name, argument_value in list_tuples_to_iterate:
                LOGGER.debug("Checking type of argument: %s", str_argument_name)
                # By default if value is None then leave this argument alone
                if argument_value is None and bool_is_to_skip_none_value:
                    continue
                for str_prefix in dict_tuple_types_by_prefix_local:
                    if str_argument_name.startswith(str_prefix):
                        check_type_of_1_argument(
                            str_function_name,
                            str_argument_name,
                            argument_value,
                            dict_tuple_types_by_prefix_local[str_prefix]
                        )

            #####
            return func_to_check(*args, **kwargs)
        return wrapper
    if function:
        return cfa_with_args(function)
    return cfa_with_args
