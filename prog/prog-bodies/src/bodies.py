import threading
import time
import sys
import os
from telnetlib import Telnet
import random

MAX_TIME = 60
FLAG = 'shctf{an-3ng1ne-0F-inn0vaTion-aNd-inspirati0n}'
bodies = []
bodies.append(b'Amalthea;\n')
bodies.append(b'Egeria;\n')
bodies.append(b'Irene;\n')
bodies.append(b'Eunomia;\n')
bodies.append(b'Psyche;\n')
bodies.append(b'Thetis;\n')
bodies.append(b'Melpomene;\n')
bodies.append(b'Fortuna;\n')
bodies.append(b'Massalia;\n')
bodies.append(b'Lutetia;\n')
bodies.append(b'Kalliope;\n')
bodies.append(b'Thalia;\n')
bodies.append(b'Themis;\n')
bodies.append(b'Phocaea;\n')
bodies.append(b'Proserpina;\n')
bodies.append(b'Euterpe;\n')
bodies.append(b'Bellona;\n')
bodies.append(b'Amphitrite;\n')
bodies.append(b'Urania;\n')
bodies.append(b'Victoria;\n')
bodies.append(b'Parthenope;\n')


def ret_l(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'L= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_adist(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'ADIST= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_angmon(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'ANGMOM= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_qr(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'QR= ')
    res = float(tn.read_very_lazy().split(b'TP=')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_rms(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'RMS= ')
    res = float(tn.read_very_lazy().split(b'\n')[0].strip(b' '))
    tn.write(b'\n')
    return res


def ret_epoch(tn, body):
    tn.read_until(b'Horizons>')
    tn.write(body)
    tn.read_until(b'Continue [ <cr>=yes, n=no, ? ] :')
    tn.write(b'\n')
    tn.read_until(b'EPOCH= ')
    res = float(tn.read_very_lazy().split(b'!')[0].strip(b' '))
    tn.write(b'\n')
    return res


def die(timeout):
    time.sleep(timeout)
    print("Time is up! sorry...")
    os._exit(0)


def intro_prompt():
    print(f"<<< You have {MAX_TIME} seconds to answer 5 questions about the ecliptic elements")
    sys.stdout.flush()


def step_prompt(step):
    sys.stdout.flush()


def main():
    intro_prompt()
    thr = threading.Thread(target=die, args=(MAX_TIME,))
    thr.start()

    print("<<< Connecting to NASA... <please wait>")
    sys.stdout.flush()
    tn = Telnet('horizons.jpl.nasa.gov', 6775)

    for i in range(0, 5):
        step_prompt(i + 1)

        rand_body = random.randint(0, len(bodies)-1)
        rand_test = random.randint(0, 5)
        if rand_test == 0:
            input_str = "Enter the <l> for %s >>> " % bodies[rand_body].strip(
                b';\n').decode()
            sol = ret_l(tn, bodies[rand_body])
        elif rand_test == 1:
            input_str = "Enter the <adist> for %s >>> " % bodies[rand_body].strip(
                b';\n').decode()
            sol = ret_adist(tn, bodies[rand_body])
        elif rand_test == 2:
            input_str = "Enter the <angmon> for %s >>> " % bodies[rand_body].strip(
                b';\n').decode()
            sol = ret_angmon(tn, bodies[rand_body])
        elif rand_test == 3:
            input_str = "Enter the <qr> for %s >>> " % bodies[rand_body].strip(
                b';\n').decode()
            sol = ret_qr(tn, bodies[rand_body])
        elif rand_test == 4:
            input_str = "Enter the <rms> for %s >>>" % bodies[rand_body].strip(
                b';\n').decode()
            sol = ret_rms(tn, bodies[rand_body])
        elif rand_test == 5:
            input_str = "Enter the <epoch> for %s >>> " % bodies[rand_body].strip(
                b';\n').decode()
            sol = ret_epoch(tn, bodies[rand_body])
        sys.stdout.flush()
        try:
            ans = float(input(input_str))
        except:
            print("<<< Incorrect. Goodbye!")
            sys.stdout.flush()
            os._exit(0)

        if (ans == sol):
            print("<<< Correct")
            sys.stdout.flush()
        else:
            print("<<< Incorrect. Goodbye!")
            sys.stdout.flush()
            os._exit(0)

    print(f"Well done! Here's your flag: {FLAG}")
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    main()
