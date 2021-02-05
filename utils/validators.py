from typing import Type

def validate_type(value: object, type: Type, key: str) -> object:
    if not isinstance(value, type):
        raise TypeError(f'{key.captalize()} must be {type}.')
    return value

def validate_not_empty(value: object, key: str) -> object:
    if not value.strip(' '):
        raise ValueError(f'{key.captalize()} can not be empty.')
    return value

def validate_length(value: object, max_length: int, key: str) -> object:
    if len(value) > max_length:
        raise ValueError(f'{key.captalize()} can not be bigger than {max_length} characteres.')
    return value
