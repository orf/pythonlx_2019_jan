import attr


@attr.s
class Point:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

    @y.validator
    def _check_y(self, attribute, value):
        if self.x == value:
            raise ValueError('x must not be the same as y')


a = Point(1, 2)
print(a)

invalid = Point(10, 10)