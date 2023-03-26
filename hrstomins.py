
import struct

hours = float(input("Please enter schedule time in 24hr format:"))
minutes = int(hours * 60)
print("Minutes = ", minutes)

minsinbinary = f'{minutes:08b}'
print(minsinbinary)

bintohex = hex(int(minsinbinary, 2))
print(bintohex)


def to_little(val):
  little_hex = bytearray.fromhex(val)
  little_hex.reverse()
  print("Byte array format:", little_hex)

  str_little = ''.join(format(x, '02x') for x in little_hex)

  return str_little

little_endian = to_little(bintohex)

print("Little endian hex:", little_endian)