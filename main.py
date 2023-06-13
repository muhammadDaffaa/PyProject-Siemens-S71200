import snap7
import snap7.util as cmd

plc = snap7.client.Client()
plc.connect('192.168.18.178',0,1) #IP PLC

print(plc.get_connected())
db_number = 4
start_offset = [0,1,2]
bit_offset = [0,1,2,3,4,5,6,7]
# value = 1  # 1 = true | 0 = false
#
# start_address = 100  # starting address
# length = 4  # double word

def readBool(db_number, start_offset, bit_offset):
    for i in start_offset:
        reading = plc.db_read(db_number, i, 1)
        for j in bit_offset:
            a = cmd.get_bool(reading, 0, j)
            print('DB Number: ' + str(db_number) + ' Bit: ' + str(i) + '.' + str(j) + ' Value: ' + str(a))

	# return None

if __name__ == '__main__':
    readBool(db_number, start_offset,bit_offset)

