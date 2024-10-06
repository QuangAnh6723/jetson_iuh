import time
import serial


ser = serial.Serial(
    port='/dev/ttyACM0',
    #port='COM3',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

__pos_init = 'init'
__pos_0 = 'pos0'
__pos_1 = 'pos1'
__pos_2 = 'pos2'

def go_pos(pos: int):
    print('robot going to',end=' ')
    if pos == 0:
        print('pos 0 ')
        # print(__pos_0)
        ser.write(b'#9P1259#11P1259#13P1017#15P845#17P1155#19P1224T500D500\r\n')
        # time.sleep(0.2)
    elif pos == 1:
        print('pos 1 ')
        # print(__pos_1)
        ser.write(b'#9P1259#11P1259#13P1017#15P741#17P1155#19P1569T500D500r\n')
        # time.sleep(0.2)
    elif pos == 2:
        print('pos 2 ')
        # print(__pos_2)
        ser.write(b'#9P1259#11P1259#13P1017#15P741#17P1155#19P2121T500D500\r\n')
        # time.sleep(0.2)
    else:
        print('pos init ')
        ser.write(b'#9P1259#11P1259#13P1017#15P845#17P1155#19P845T500D500\r\n')
    # time.sleep(0.2)


def init():
    print(init.__name__)
    go_pos(-1)
