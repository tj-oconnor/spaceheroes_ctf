from pwn import *
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from io import StringIO

p = remote('0.cloud.chals.io', 29511)

p.recvuntil(b"=================================== StarFleet Intelligence Reports==============================================")

train_fet = open('training_features.txt', 'w')
train_lab = open('training_labels.txt', 'w')

while True:
    res = p.recvline()
    if b'==========================================================' in res:
        break
    if (len(res) > 2):
        label = res.split(b']')[1].replace(b'\n', b'').replace(b' ', b'')
        feature = res.split(b']')[0].replace(b'[', b'')
        print(feature, label)
        train_fet.write(feature.decode()+"\n")
        train_lab.write(label.decode()+"\n")

train_fet.close()
train_lab.close()

training_fet = pd.read_csv('training_features.txt', header=None)
training_lab = pd.read_csv('training_labels.txt', header=None)

print(training_lab)

clf = RandomForestClassifier()
clf.fit(training_fet, training_lab[0])


cnt = 0
while True:
    p.recvuntil(b'A ship approaches: ')
    res = p.recvline()
    feature = res.split(b"[")[1].split(b"]")[0]
    data = StringIO(str(feature, 'utf-8'))
    df_feature = pd.read_csv(data, header=None)

    predicted_ship = clf.predict(df_feature)
    print("Predicted Vessel: %s" % predicted_ship)
    if "Starfleet" in str(predicted_ship):
        p.sendline(b"N")
    else:
        p.sendline(b"Y")
    print(p.recvline())
    cnt += 1
    if (cnt == 25):
        break

p.interactive()
