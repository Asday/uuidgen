from functools import partial
from random import randint  # noqa
import string

import numpy as np


# https://stackoverflow.com/a/48421303/1149933
def produce_amount_keys(amount_of_keys, _randint=np.random.randint):
    keys = set()
    pickchar = partial(
        np.random.choice,
        np.array(list(string.ascii_uppercase + string.digits)))
    while len(keys) < amount_of_keys:
        keys |= {''.join([pickchar() for _ in range(_randint(12, 20))]) for _ in range(amount_of_keys - len(keys))}  # noqa
    return keys
