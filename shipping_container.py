"""
Shipping Container Classes
"""
import iso6346

class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    next_serial = 1337

    def __init__(self, owner_code, length_ft, contents):
        self._owner_code = owner_code
        self._length_ft = length_ft
        self._contents = contents
        self._bic = self._make_bic_code(
            owner_code=owner_code,
            serial=self._get_next_serial())

    # we can use a @classmethod instead
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self._length_ft


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature is too hot!")
        self._celsius = value

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    # Task: Add support to Read+Write fahrenheit
    @property
    def fahrenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratorShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return (self._length_ft
                * ShippingContainer.HEIGHT_FT
                * ShippingContainer.WIDTH_FT
                - RefrigeratorShippingContainer.FRIDGE_VOLUME_FT3)


class HeatedRefrigeratedShippingContainer(RefrigeratorShippingContainer):
    MIN_CELSIUS = -20.0

    # @celsius.setter  # out of scope
    @RefrigeratorShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature is too cold")
        # self._celsius = value
        RefrigeratorShippingContainer.celsius.fset(self,value)

if __name__ == '__main__':
    h1 = HeatedRefrigeratedShippingContainer.create_empty(owner_code="YML", length_ft=40,
                                                          celsius=-15)
    print(h1.__dict__)


    # c1 = ShippingContainer(owner_code="MAE",
    #                        contents="fruit",
    #                        length_ft=20)
    # print(c1.volume_ft3)
    #
    # r1 = RefrigeratorShippingContainer.create_empty(owner_code='YML',
    #                                                 length_ft=25,
    #                                                 celsius=1.0 )
    # print(r1.volume_ft3)