from base64 import b64encode
from random import choice, randint
from string import ascii_uppercase, digits
from uuid import uuid4


ALLOWED_CHARS = [char.encode() for char in ascii_uppercase + digits]


def uuidgen(count):
    generated = set()

    while True:
        if len(generated) == count:
            return

        candidate = b64encode(
            uuid4().int.to_bytes(16, 'little'),
            b'//',
        ).upper()[:randint(12, 20)]

        while b'/' in candidate:
            candidate = candidate.replace(b'/', choice(ALLOWED_CHARS), 1)

        if candidate not in generated:
            generated.add(candidate)
            yield candidate
