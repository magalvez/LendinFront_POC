import base64, os
from Crypto.Cipher import AES
from Crypto import Random


BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s)-1:])]

SECRET_KEY = os.environ.get('SECRET_KEY') or "lfdsjkEERkjkW1jk$5Jk%#1q2dsfdsaS"

class AESCipher:
    """
        AES: Advanced Encryption Standard
        Uses blocks to encrypt and decrypt each input
    """

    def __init__(self, key=None):
        self.key = key if key is not None else SECRET_KEY

    def encrypt(self, encryption_input):
        encryption_input = pad(encryption_input)
        # Avoid the issue https://github.com/dlitz/pycrypto/issues/136
        # when this library is called with a multi processes approach
        Random.atfork()
        encryption_output = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, encryption_output)
        return base64.b64encode(encryption_output + cipher.encrypt(encryption_input))

    def decrypt(self, decryption_input):
        decryption_input = base64.b64decode(decryption_input)
        decryption_output = decryption_input[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, decryption_output)
        return unpad(cipher.decrypt(decryption_input[16:]))

    def decrypt_masked(self, decryption_input, num_unmasked):
        un_masked = self.decrypt(decryption_input)
        masked = ""
        if len(un_masked) > num_unmasked:
            num_masks = len(un_masked) - num_unmasked
            partial_un_masked = un_masked[-num_unmasked:]
            masked = ('X' * ((num_masks/len('X'))+1))[:num_masks] + partial_un_masked
        else:
            num_masks = len(un_masked)
            masked = ('X' * ((num_masks/len('X'))+1))[:num_masks]
        return masked


def decrypt_value(value):
    """
    Decrypt the given value
    :param value: String, value to decrypt
    :return: String
    """
    if value not in [None, '']:
        if len(value) == 4:
            return value
        cyfrer = AESCipher()
        decrypted_value = cyfrer.decrypt(value)
        return decrypted_value
    return None
