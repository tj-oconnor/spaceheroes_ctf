import cv2

vidcap = cv2.VideoCapture('buzzsaw.avi')
count = 0
flag = ''
bit_pos = [355, 390, 425, 460, 495, 530, 565, 600]
success = True

while success:
    success, image = vidcap.read()
    if success:
        bits = ''
        for bit in bit_pos:
            _, green, red = image[700, bit]
            if red < 250:
                if green < 250:
                    bits = bits+'0'
                else:
                    bits = bits+'1'
        flag = flag+chr(int(bits, 2))
        count = count+1
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)
    else:
        vidcap.release()
        print(flag)
        break
