from timeit import timeit

from implementations.uuidgen import uuidgen
from implementations.produce_amount_keys import produce_amount_keys


# print('Timing 40k keys 10 times with produce_amount_keys, stdlib randint')
# print(timeit(
#     stmt='produce_amount_keys(40000, _randint=randint)',
#     setup='from __main__ import produce_amount_keys; from random import randint',  # noqa
#     number=10,
# ))

print('Timing 40k keys 10 times with uuidgen, stdlib randint')
print(timeit(
    stmt='list(uuidgen(40000))',
    setup='from __main__ import uuidgen',
    number=10,
))
