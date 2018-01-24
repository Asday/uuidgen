from base64 import b64encode
from math import ceil
from os import urandom
from random import choice, randint
from string import ascii_uppercase, digits


ALLOWED_CHARS = [char.encode() for char in ascii_uppercase + digits]


def urandomgen(count):
    generated = set()

    while True:
        if len(generated) == count:
            return

        desired_length = randint(12, 20)

        # # Faster than math.ceil
        # urandom_bytes = urandom(((desired_length + 1) * 3) // 4)
        #
        # candidate = b64encode(urandom_bytes, b'//').upper()
        #
        # The above is rolled into one line to cut down on execution
        # time stemming from locals() dictionary access.

        candidate = b64encode(
            urandom(((desired_length + 1) * 3) // 4),
            b'//',
        ).upper()[:desired_length]

        while b'/' in candidate:
            candidate = candidate.replace(b'/', choice(ALLOWED_CHARS), 1)

        if candidate not in generated:
            generated.add(candidate)
            yield candidate.decode()
