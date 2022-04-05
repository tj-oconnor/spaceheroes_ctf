from flask import Flask, redirect, url_for
import base64
import uuid as uu

app = Flask(__name__)

flag = ["~"]

uuids = {}


@app.before_first_request
def readFlag():
    global flag
    with open("flag.txt", "rb") as flagf:
        byt = base64.b64encode(flagf.read())
        for char in byt:
            flag += [f"{b}" for b in list(f"{char & 0xFF:07b}")]


@app.route("/seq/<uuid>")
def serveSequence(uuid):
    global uuids
    try:
        x = uuids[uuid]
        uuids[uuid] += 1
        ret = flag[x % len(flag)]
        return ret
    except KeyError as e:
        return "ID NOT FOUND"


@app.route('/')
def hello_world():  # put application's code here
    uuid = str(uu.uuid4())
    uuids[uuid] = 0
    return redirect(url_for("serveSequence", uuid=uuid))


if __name__ == '__main__':
    readFlag()
    app.run(host="0.0.0.0")
