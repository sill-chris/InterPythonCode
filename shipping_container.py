"""
Shipping Container Classes
"""
import iso6346

class ShippingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())


    # we can use a @classmethod decorator instead
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result


    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code,contents=list(items))


    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              )


if __name__ == '__main__':
    c1 = ShippingContainer("MAE", "fruit")
    print(c1._bic)
    # print(ShippingContainer.next_serial)
    c2 = ShippingContainer.create_empty("YML")
    print(c2._bic)
    c3 = ShippingContainer.create_with_items("ABC", ["food",
                                             "textiles", "minerals"])
    print(c3._bic)
