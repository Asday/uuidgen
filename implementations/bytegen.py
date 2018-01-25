from os import urandom
from random import randint
from string import ascii_uppercase, digits

# Masks for extracting the numbers we want from the maximum possible
# length of `urandom_bytes`.
bitmasks = [(0b111111 << (i * 6), i) for i in range(15)]
allowed_chars = (ascii_uppercase + digits) * 16  # 576 chars long


def bytegen(count):
    generated = set()

    while True:
        if len(generated) == count:
            return

        # Generate 9 characters from 9x6 bits
        desired_length = randint(12, 20)
        bytes_needed = (((desired_length * 6) - 1) // 8) + 1

        # Endianness doesn't matter.
        urandom_bytes = int.from_bytes(urandom(bytes_needed), 'big')

        chars = [
            allowed_chars[
                (((urandom_bytes & bitmask) >> (i * 6)) + (0b111111 * i)) % 576
            ]
            for bitmask, i in bitmasks
        ][:desired_length]

        candidate = ''.join(chars)

        if candidate not in generated:
            generated.add(candidate)
            yield candidate
