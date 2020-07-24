# Standard library imports
import sys
import logging
# Third party imports

# Local imports


LOGGER = logging.getLogger("check_function_arguments")
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


def check_type_of_1_argument(
        str_function_name,
        str_argument_name,
        argument_value,
        tuple_types_var_can_be
):
    """"""
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
    raise TypeError(str_error_message)


def cat(
        function=None,
        dict_tuple_types_by_prefix=None,
        dict_tuple_types_by_prefix_to_update_default=None,
        bool_is_to_skip_None_value=True,
):
    """"""
    if dict_tuple_types_by_prefix is None:
        dict_tuple_types_by_prefix_local = DICT_TUPLE_DEFAULT_TYPES_BY_PREFIX
    else:
        dict_tuple_types_by_prefix_local = dict_tuple_types_by_prefix

    def cfa_with_args(func_to_check):
        """"""
        int_args_count = func_to_check.__code__.co_argcount
        list_function_arguments = \
            func_to_check.__code__.co_varnames[:int_args_count]
        str_function_name = func_to_check.__name__

        def wrapper(*args, **kwargs):
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
                if argument_value is None and bool_is_to_skip_None_value:
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

