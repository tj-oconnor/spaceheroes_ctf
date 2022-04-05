import bitstring

def shift_check( filename ):
    f = open(filename, 'rb')
    bits = bitstring.Bits( f )
    f.close()
    bits_array = bitstring.BitArray( bits )
    skip =8*3
    for k in range(8):
        start = k + skip
        stop  = start+  200*8
        shifted = bits_array[start:stop]
        byte_data = shifted.bytes
        try:
            print("offset {}".format(k))
            print( byte_data.decode('utf-8'))
        except:
            print("Not ascii at offset {}".format(k))
            pass
        


if __name__ == "__main__":
    shift_check("out.txt")