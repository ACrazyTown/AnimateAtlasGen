from fla import *

#fla.unpack("./test.fla")
fla = FLADocument("./input/test - Copy - Copy.fla")
print(fla.LIBRARY.get_contents())