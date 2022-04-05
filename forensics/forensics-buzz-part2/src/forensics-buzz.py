import cv2
import binascii

flag = "shctf{Sh3r1ff-tH1s-is-n0-t1m3-t0-pAn1c}"
original_f = "buzz.png"
output_video = "buzz.mp4"


def clock_bits(input_f):
    img = cv2.imread(input_f)
    bit_pos = [355, 390, 425, 460, 495, 530, 565, 600]
    for i in range(0, 8):
        cv2.circle(img, (bit_pos[i], 696), 15, (149, 53, 83), 3)
        cv2.circle(img, (bit_pos[i], 696), 15, (0, 0, 255), -1)
    return img


def encode_bits(input_f, bits):
    img = cv2.imread(input_f)
    bit_pos = [355, 390, 425, 460, 495, 530, 565, 600]
    for i in range(0, 8):
        cv2.circle(img, (bit_pos[i], 696), 15, (149, 53, 83), 3)
        if bits[i] == '1':
            cv2.circle(img, (bit_pos[i], 696), 15, (0, 255, 0), -1)
    return img


img = cv2.imread(original_f)
height, width, layers = img.shape
size = (width, height)
img_array = []


f = open('fuzz', 'rb')

while True:
    try:
        x = f.read(1)
        bits = '{:08b}'.format(ord(x))
        # print(bits)
        img = encode_bits(original_f, bits)
        clock = clock_bits(original_f)
        img_array.append(clock)
        img_array.append(img)
    except:
        break

video_out = cv2.VideoWriter(
    'buzzsaw.avi', cv2.VideoWriter_fourcc(*'mp4v'), 100, size)

for i in range(len(img_array)):
    video_out.write(img_array[i])

video_out.release()
