import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():

    limite = 100
    resul = 0
    numeros = []
    primos = ""

    while True:
        cdp = 0
        for b in range(1, resul+1):
            if resul % b == 0:
                cdp += 1
        if cdp == 2:
            numeros.append(resul)
            primos += str(resul) + ", "
        if len(numeros) == 100:
            break
        resul += 1

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
