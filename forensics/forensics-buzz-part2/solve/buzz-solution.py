import cv2
import sys

vidcap = cv2.VideoCapture(sys.argv[1])
count = 0
flag = ''
bit_pos = [355, 390, 425, 460, 495, 530, 565, 600]
success = True

print("[+] Opening Flag File")
flag_file = open('flag.bin', 'wb')

print("[+] Looping Through Images")

cnt = 0
clock = True
while success:
    success, image = vidcap.read()
    if success:
        bits = ''
        for bit in bit_pos:
            _, green, red = image[700, bit]
            if red < 250:
                clock = False
                if green < 250:
                    bits = bits+'0'
                else:
                    bits = bits+'1'
                cnt += 1
            else:
                clock = True
        if (not clock):
            flag_file.write(int(bits, 2).to_bytes(1, 'big'))
        count = count+1
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)
    else:
        vidcap.release()
        flag_file.close()
        break
