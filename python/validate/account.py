import logging

logging.basicConfig(level=logging.INFO)

def validate(code):
    logging.info('***************************')
    logging.info('code:{}'.format(code))

    account_hex_str = code[:-2]
    logging.info('account hex:{}'.format(account_hex_str))

    account_checksum_hex_str = code[-2:]
    logging.info('account checksum hex:{}'.format(account_checksum_hex_str))

    account_dec = int(account_hex_str, 16)
    logging.info('account dec:{}'.format(account_dec))

    account_checksum_dec = sum([int(i) for i in str(account_dec)])
    logging.info('account checksum dec:{}'.format(account_checksum_dec))

    encoded_account_checksum_hex_str = '{:x}'.format(account_checksum_dec)
    logging.info('decoded account checksum:{}'.format(encoded_account_checksum_hex_str))

    if account_checksum_hex_str.lower()  == encoded_account_checksum_hex_str.lower():
        return 'VALID'
    else:
        return 'INVALID'


if __name__ == '__main__':
    print(validate('8BADF00D'))
    print(validate('C0FFEE1C'))






