# Standard library imports
# Third party imports

# Local imports
from cat.main import cat

check_arguments_types = cat
__all__ = ["cat", "check_arguments_types"]


#####
# Prepare basic logger in case user is not setting it itself.
#####
import logging
LOGGER = logging.getLogger("check_arguments_types")
LOGGER.addHandler(logging.NullHandler())

