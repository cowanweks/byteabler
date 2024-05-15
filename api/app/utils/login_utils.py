from bcrypt import hashpw, gensalt, checkpw


def hash_password(password: str) -> str:
    """A helper function that verifies user password against the hash"""

    salt = gensalt()
    pwd = password.encode()

    # Hash the password
    hashed_pwd = hashpw(pwd, salt)
    return hashed_pwd.decode()


def verify_password(password: str, hash: bytes) -> bool:
    """A helper function that verifies user password against the hash"""

    if checkpw(password.encode(), hash):
        return True

    return False
