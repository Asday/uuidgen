from base64 import b64encode
from functools import partial
from random import randint  # noqa
import string
from timeit import timeit
from uuid import uuid4

import numpy as np


def uuidgen(count, _randint=np.random.randint):
    generated = set()

    while True:
        if len(generated) == count:
            return

        candidate = b64encode(uuid4().hex.encode()).upper()[:_randint(12, 20)]
        if candidate not in generated:
            generated.add(candidate)
            yield candidate


# https://stackoverflow.com/a/48421303/1149933
def produce_amount_keys(amount_of_keys, _randint=np.random.randint):
    keys = set()
    pickchar = partial(
        np.random.choice,
        np.array(list(string.ascii_uppercase + string.digits)))
    while len(keys) < amount_of_keys:
        keys |= {''.join([pickchar() for _ in range(_randint(12, 20))]) for _ in range(amount_of_keys - len(keys))}  # noqa
    return keys


def benchmark():
    print('Timing 40k keys 10 times with produce_amount_keys')
    print(timeit(
        stmt='produce_amount_keys(40000)',
        setup='from __main__ import produce_amount_keys',
        number=10,
    ))

    print('Timing 40k keys 10 times with produce_amount_keys, stdlib randint')
    print(timeit(
        stmt='produce_amount_keys(40000, _randint=randint)',
        setup='from __main__ import produce_amount_keys; from random import randint',  # noqa
        number=10,
    ))

    print('Timing 40k keys 10 times with uuidgen')
    print(timeit(
        stmt='list(uuidgen(40000))',
        setup='from __main__ import uuidgen',
        number=10,
    ))

    print('Timing 40k keys 10 times with uuidgen, stdlib randint')
    print(timeit(
        stmt='list(uuidgen(40000, _randint=randint))',
        setup='from __main__ import uuidgen; from random import randint',
        number=10,
    ))
