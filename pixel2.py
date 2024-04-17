from PIL import Image
import numpy as np

hacked = np.asarray(Image.open('hacked.png'))

biale =                 '3C000001030001330000007054000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009194C'
jazda_probna =          '5900000103000150000304494E1163627A189819413141303A3563224124562904727A17A81941314130300703413141314553A03323114341643B537215112511835C043132313A1313A0362525250398194131413031E738'
poziome =               'B7000001010001AE0000003054555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555064F'
kratka =                'B7000001010001AE00000030545555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAA5555AAAAF32C'
pionowe =               '620000010100015900000070530101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101E12B'

test =                  '4B000001030001420000007070000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007'
testo =                 '3C000001030001330000007054796D2D2D0000000000000000000000000000000000000000000000000000000000000000000000000000000000'
przerwa_na_posilek =    '91 00 00 01 03 00 01 88 00 09 00 70 43 796D2D2D6970379D61285121312154312162179604797B221A321921B213217C121C1212241342331423112219122119133153149915191512E271531212191212191511122A2149121212821212B124221122143219214913217970379E324742311262412248870027261728212151222121512251279602797B3C212A23291519A494'
przejazd_tech =         '9E 00 00 01 05 00 01 95 00 06 00 50 49 61F19797F1F12797C12851285521216211212191510379715522833225122155121321232A131042419338211228212211315133315149970379E21212731212132415122D697314192419158215827A6025A7261151285151233251211131379602241933122421221233222112112223321221242213391420179637324722515116215835C3073C493D3014D390F8D7'
pixel =                 '46 00 00 01 03 00 01 3D 00 0D 02 6D 3B 0094252425242524333495775000900900071B39668351C3874774B15396593B1000700B3244324432443244324492000700BB2B2B2B2B7C84'
test1 =                 '39 00 02 01 03 00 01 30 00 00 00 70 43 100000000000000000000000000000000000000000000000000000000000000000000000000000000000'
toruń =                 '6E 00 00 01 03 00 01 65 00 06 01 4F 49 C2D2D21E1ED2D2D203A4C238312A212A212A213832C4A03E1E7242634245422413231346217405C2D13C2D2D2D3DD3C01E1EA3A3316352248F1E00000003A4C238312A21242421242421332332723462203E1E1232824272526262520D2D2D' #4FB0'
pesa =                  '9D 00 00 01 05 00 01 94 00 03 00 50 4E 179791212191212197A21200E3A114A111D6B500E3C5B131B79700D2B114A11121A6371447C121C121237415722131B5C34797912121112141212111133151111111B311C1214122A21491212112213121211311341211134221212200563347156121113161211131379603221B311B113B1220000002122A2149121219121219412A22100C6A7C121C12197969' #1882'
esp32 =                 '1F 00 00 01 03 00 01 16 00 00 00 50 10 1F1E1E1E1E1E1E1E1E1E1E1E1E1E1E1EF713'
# ^42b data, 48b 2nd size, 57b 1st size
#1074 dots
# 0 means 15 dots, next nibble goes the same colour, F means 15 dots, next nibble changes colour

#hdr[11] = 0:4 - rows, 5: white or black, 6:7 - 0b01

base = 'FF00FE01030001FF00FC00FBFD'
data = '110000000000000000000000000000000000000000000000000000000000000000000000'

import time
from pixel import Pixel

px = Pixel('/dev/tty.wchusbserial55860074291')
px.open()
datablock = px.create_data_block(px.get_image_data('ts100noga.bmp', invert=True))
px.display_data_block(0, datablock)

time.sleep(0.1)

datablock = px.create_data_block(px.get_image_data('hacked.png', invert=True, page=1))
px.display_data_block(0, datablock)

time.sleep(0.1)

datablock = px.create_data_block(px.get_image_data('krakow.png', invert=True, page=2))
px.display_data_block(0, datablock)
time.sleep(15)
print("wooohooo")
px.delete_all_pages(0)
datablock = px.create_data_block(px.get_image_data('papa.png', invert=False))
px.display_data_block(0, datablock)
time.sleep(0.2)
datablock = px.create_data_block(px.get_image_data('ts100viron.bmp', invert=True, page=1))
px.display_data_block(0, datablock)
# px.send_sat()
# px.send_sat()
# px.send_sat()
# px.delete_page(1, '01FF5F')

exit()
#px.delete_page(2, '01FF5F')
#px.send_sat()
#time.sleep(0.2)
#px.delete_page(0, '01FF5F')
#time.sleep(0.2)

hdr = bytearray.fromhex(base)
dt = bytearray.fromhex(data)
_1stSize = len(dt) + 15
_2ndSize = len(dt) + 6
screen = 0
leftOffset = 6
bottomOffset = 0
columnCount = 0x43

rowCount = 16
startWith = True
cfg = (rowCount & 0x1f) | ((1 if startWith else 0) << 5) | 0b01000000

hdr[0] = _1stSize
hdr[2] = screen
hdr[7] = _2ndSize
hdr[9] = leftOffset
hdr[10] = bottomOffset
hdr[11] = cfg
hdr[12] = columnCount

block = bytes(hdr + dt)


#datablock = px.create_data_block(bytes.fromhex(przerwa_na_posilek))
datablock = px.create_data_block(block)
px.display_data_block(0, datablock)
exit()


datablock = px.create_data_block(px.get_image_data('ts100noga.bmp', invert=True))
px.display_data_block(2, datablock)

time.sleep(0.1)

datablock = px.create_data_block(px.get_image_data('hacked.png', invert=True, page=3))
px.display_data_block(2, datablock)

time.sleep(0.1)

datablock = px.create_data_block(px.get_image_data('krakow.png', invert=True, page=4))
px.display_data_block(2, datablock)

time.sleep(0.1)

datablock = px.create_data_block(px.get_image_data('papa.png', invert=False, page=5))
px.display_data_block(2, datablock)

#time.sleep(0.1)
#px.set_whole_matrix(0, True)