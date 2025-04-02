from enum import Enum
from PIL import Image

consts = [
    (3, [0x01]),
    (4, [0x01, 0x03, 0x05]),
    (5, [0x00]),
    (6, [0x01]), # in fact not a const, but number of images in this message. Will fix someday.
    (10, [0x00])
]

class EncodingType(Enum):
    Bitmap = 1
    Nibble = 2

    def from_setup(setup: int):
        return EncodingType(((setup >> 6) & 0x03) + 1)

inp = input("Data Block: ")
data = bytearray.fromhex(inp)
l0 = data[0] | (data[1] << 8)
if l0 != len(data):
    print("Packet length doesn't make sense")
    exit()
if l0 < 15:
    print("Packet is too short. Idk how would you manage it in less than 15 bytes.")
    exit()

for c in consts:
    ix = c[0]
    if not data[ix] in c[1]:
        print(f'Unknown const at position {ix}, expected {c[1]}, found {data[ix]}')

l7 = data[7] | (data[8] << 8)
page = data[2]
l_offset = data[9]
b_offset = data[10]
setup = data[11]
rows = setup & 0x1F
invert = ((setup >> 5) & 0x01) > 0
encoding = EncodingType.Bitmap #EncodingType.from_setup(setup)
columns = data[12]

print(f'ImgData: \n\tPage: {page}\n\tLeft: {l_offset}\n\tBottom: {b_offset}\n\tRows: {rows}\n\tColumns: {columns}\n\tInvert: {invert}\n\tEncoding: {encoding}')

image = Image.new('1', (500, rows))

def decode_bitmap() -> int:
    ix = 13
    on = 1 if not invert else 0
    off = 0 if not invert else 1
    cx = 0
    cy = rows - 1
    while ix < l0 - 2:
        for bit in range(8):
            isOn = (data[ix] & (1 << bit)) > 0
            image.putpixel((cx, rows - cy - 1), on if isOn else off)
            if cy == 0:
                cy = rows - 1
                cx += 1
            else:
                cy -= 1
        ix += 1
    return cx
def draw_nibble(nibble: int, x: int, y: int, color: int) -> tuple[int, int, int]:
    newColor = color
    cx = x
    cy = y
    count = nibble if nibble != 0 else 15

    while count > 0:
        image.putpixel((cx, cy), newColor)
        if cy == 0:
            cy = rows - 1
            cx += 1
        else:
            cy -= 1
        count -= 1

    if nibble != 0:
        newColor = 0 if color == 1 else 1
    return (cx, cy, newColor)
def decode_nibble() -> int:
    ix = 13
    color = 0 if invert else 1
    x = 0
    y = rows - 1
    while ix < l0 - 2:
        (x, y, color) = draw_nibble((data[ix] & 0xf0) >> 4, x, y, color)
        (x, y, color) = draw_nibble((data[ix] & 0x0f), x, y, color)
        ix += 1
    return x

finalColumns = 1
if encoding == EncodingType.Bitmap:
    finalColumns = decode_bitmap()
elif encoding == EncodingType.Nibble:
    finalColumns = decode_nibble()

print(finalColumns)
if finalColumns == 0:
    print("Something's not right if there are no columns...")
    exit()
result = image.crop((0, 0, finalColumns, rows))
result.show()
