from os import urandom
from random import randint
from string import ascii_uppercase, digits

# Masks for extracting the numbers we want from the maximum possible
# length of `urandom_bytes`.
bitmasks = [(0b111111 << (i * 6), i) for i in range(15)]


def bytegen_nostring_maths(count):
    generated = set()

    while True:
        if len(generated) == count:
            return

        # Generate 9 characters from 9x6 bits
        desired_length = randint(12, 20)
        bytes_needed = (((desired_length * 6) - 1) // 8) + 1

        # Endianness doesn't matter.
        urandom_bytes = int.from_bytes(urandom(bytes_needed), 'big')

        indices = (
            ((((urandom_bytes & bitmask) >> (i * 6)) + (0b111111 * i)) % 576) % 36  # noqa
            for bitmask, i in bitmasks
        )

        candidate = bytes([
            index + 65 if index < 26 else index + 22
            for index in indices
        ][:desired_length])

        if candidate not in generated:
            generated.add(candidate)
            yield candidate.decode()
