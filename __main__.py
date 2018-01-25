from timeit import timeit

from implementations.bytegen import bytegen
from implementations.bytegen_nostring import bytegen_nostring
from implementations.bytegen_nostring_maths import bytegen_nostring_maths
from implementations.produce_amount_keys import produce_amount_keys
from implementations.urandomgen import urandomgen
from implementations.uuidgen import uuidgen


print('Timing 40k keys 10 times with produce_amount_keys, stdlib randint')
print(timeit(
    stmt='produce_amount_keys(40000, _randint=randint)',
    setup='from __main__ import produce_amount_keys; from random import randint',  # noqa
    number=10,
))

print('Timing 40k keys 10 times with uuidgen, stdlib randint')
print(timeit(
    stmt='list(uuidgen(40000))',
    setup='from __main__ import uuidgen',
    number=10,
))

print('Timing 40k keys 10 times with urandomgen, stdlib randint')
print(timeit(
    stmt='list(urandomgen(40000))',
    setup='from __main__ import urandomgen',
    number=10,
))

print('Timing 40k keys 10 times with bytegen, stdlib randint')
print(timeit(
    stmt='list(bytegen(40000))',
    setup='from __main__ import bytegen',
    number=10,
))

# print('Timing 40k keys 10 times with bytegen_nostring, stdlib randint')
# print(timeit(
#     stmt='list(bytegen_nostring(40000))',
#     setup='from __main__ import bytegen_nostring',
#     number=10,
# ))
#
# print('Timing 40k keys 10 times with bytegen_nostring_maths, stdlib randint')
# print(timeit(
#     stmt='list(bytegen_nostring_maths(40000))',
#     setup='from __main__ import bytegen_nostring_maths',
#     number=10,
# ))
