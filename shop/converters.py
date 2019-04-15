class FourDigitYearConverter:
    regex = r'\d{4}'

    def to_python(self, value): #  method, which handles converting the matched string into the type that should be passed to the view function. It should raise ValueError if it can’t convert the given value.
        return int(value)

    def to_url(self, value): # method, which handles converting the Python type into a string to be used in the URL.
        return '%04d' % value
        