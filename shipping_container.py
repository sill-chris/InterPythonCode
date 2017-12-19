"""
Shipping Container Classes
"""


class ShippingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1