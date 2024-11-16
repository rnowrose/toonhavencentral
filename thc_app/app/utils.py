import hashlib


def generate_fake_checksum(value):
    return hashlib.md5(value.encode()).hexdigest()
