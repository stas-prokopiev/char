# Standard library imports

# Third party imports

# Local imports
from char.main import char

check_arguments = char
check_types_of_arguments = char
__all__ = ["char", "check_arguments", "check_types_of_arguments"]


#####
# Prepare basic logger in case user is not setting it itself.
#####
import logging
LOGGER = logging.getLogger("check_types_of_arguments")
LOGGER.addHandler(logging.NullHandler())

