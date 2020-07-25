====
char
====

.. image:: https://img.shields.io/github/last-commit/stas-prokopiev/char
   :target: https://img.shields.io/github/last-commit/stas-prokopiev/char
   :alt: GitHub last commit

.. image:: https://img.shields.io/github/license/stas-prokopiev/char
    :target: https://github.com/stas-prokopiev/char/blob/master/LICENSE.txt
    :alt: GitHub license<space><space>

.. image:: https://readthedocs.org/projects/char/badge/?version=latest
    :target: https://char.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/stas-prokopiev/char.svg?branch=master
    :target: https://travis-ci.org/stas-prokopiev/char

.. image:: https://img.shields.io/pypi/v/char
   :target: https://img.shields.io/pypi/v/char
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/char
   :target: https://img.shields.io/pypi/pyversions/char
   :alt: PyPI - Python Version


.. contents:: **Table of Contents**

Overview.
=========================
char stands for: check of arguments.

| This library gives to user ability to check types of function arguments via one decorator
| if your team have some agreements how to name variables with defined types
| Or if you are ready to use mine (they will be described bellow)
| This can prevent many errors

Example
------------------------------

| Let's say that you defined a function **func(int_x)** and you want to check
| if value that is given to variable **int_x** has type int
| Usually you would have to check it yourself somehow like this: **isinstance(int_x, int)**
| But with this decorator this can be done for you automatically.
| And if type of given value is wrong, then you'll get a nice exception with description

.. code-block:: python

    from char import char
    # OR from char import check_types_of_arguments  # They are equivalent

    @char
    def func(int_x):
        pass


| If you try to call function with wrong types of arguments: **func("pewpew")**
| you'll get an error like this:

.. code-block:: bash

    ArgumentTypeError: Incorrect type of variable was given to function: func
    ---> For variable: int_x
    ---> Were given value: pewpew
    ---> With type: <class 'str'>
    ---> Instead of: <class 'int'>

Installation via pip:
======================

.. code-block:: bash

    pip install char

Usage with default settings
============================

Default prefices
------------------------------
**Here will be a list of name prefices and which type the variable is expected to be**

If prefix of variable name doesn't satisfy any of the given, then variable won't be checked.

#. "any_" -  object
#. "bool_" -  bool
#. "b_" -  bool
#. "is_" -  bool
#. "has_" -  bool
#. "str_" -  str
#. "bytes_" -  bytes
#. "int_" -  int
#. "i_" -  int
#. "float_" -  float
#. "f_" -  float
#. "list_" -  list
#. "l_" -  list
#. "dict_" -  dict
#. "d_" -  dict
#. "set_" -  set
#. "tuple_" -  tuple
#. "t_" -  tuple

Example
------------------------------

.. code-block:: python

    from char import char

    @char
    def oh_my_god(
            int_arg,
            float_arg,
            list_arg,
            undef_arg,
            d_kwarg=None,
            i_kwarg=0,
            is_kwarg=False
    ):
        pass

    oh_my_god(0, 0.0, [], 1)  # Will PASS
    oh_my_god(0, 0.0, None, "text")  # Will PASS
    oh_my_god(0, 0.0, {}, "text")  # Will FAIL and raise an ArgumentTypeError
    oh_my_god(0, 0.0, [], Exception, d_kwarg={0: 1})  # Will PASS
    oh_my_god(0, 0.0, [], object, is_kwarg=0)  # Will FAIL and raise an ArgumentTypeError


Usage with user defined settings
===================================================================

Decorator arguments
--------------------------------------------------------------------------------------------------

#. **bool_is_to_skip_None_value=True**: Flag what to do with None values, by default None values won't be checked.
#. **dict_tuple_types_by_prefix_to_update_default**: dictionary, which prefices to add to the default ones
#. **dict_tuple_types_by_prefix**: dictionary, which prefices to use instead of default ones

Decorator argument **bool_is_to_skip_None_value**
--------------------------------------------------------------------------------------------------

.. code-block:: python

    @char
    def func_with_default_decorator(dict_x):
        pass

    @char(bool_is_to_skip_None_value=False)
    def func_with_custom_decorator(dict_x):
        pass

    func_with_default_decorator(None)  # Will PASS
    func_with_custom_decorator(None)  # Will FAIL and raise an ArgumentTypeError


Decorator argument **dict_tuple_types_by_prefix_to_update_default**
--------------------------------------------------------------------------------------------------

.. code-block:: python

    @char(dict_tuple_types_by_prefix_to_update_default={"num_": (int, float, bool)})
    def very_complex_function(num_x, str_y=""):
        pass

    very_complex_function(0, "hihi")  # Will PASS
    very_complex_function(0.5, "heyhey")  # Will PASS
    very_complex_function(True)  # Will PASS
    very_complex_function("True")  # Will FAIL and raise an ArgumentTypeError

Decorator argument **dict_tuple_types_by_prefix**
--------------------------------------------------------------------------------------------------

.. code-block:: python

    @char(dict_tuple_types_by_prefix={"exception": (BaseException)})
    def function_with_only_one_check(int_x, exception_y=None):
        pass

    function_with_only_one_check(0, Exception)  # Will PASS
    function_with_only_one_check(0.5, TypeError)  # Will PASS because first variable won't be checked
    function_with_only_one_check(0.5, "ERROR")  # Will FAIL and raise an ArgumentTypeError

Links
=====

    * `PYPI <https://pypi.org/project/char/>`_
    * `readthedocs <https://char.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/stas-prokopiev/char>`_

Project local Links
===================

    * `CHANGELOG <https://github.com/stas-prokopiev/char/blob/master/CHANGELOG.rst>`_.
    * `CONTRIBUTING <https://github.com/stas-prokopiev/char/blob/master/CONTRIBUTING.rst>`_.

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.

