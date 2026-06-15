import datetime
import time

# TODO: Format time:
# Example
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
# Oct 21 2022

epoch = time.time()
date = datetime.datetime.fromtimestamp(epoch)

# f-string formatting
# {varname: } - format specifier
# :, - comma separator for large numbers
# :. - precision for floating point numbers
# :e - scientific notation with exponent
# :.<number>f - precision for floating point numbers
print(
    f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} "
    + "in scientific notation\n"
    + f"{date.strftime('%b %d %Y')}"
)
