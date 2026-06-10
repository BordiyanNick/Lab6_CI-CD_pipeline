# Модель: Математичне моделювання біологічного росту бактерій (5 семестр)
# Автор: Бордіян Микола Павлович, група AI-231

import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

class BacteriaGrowthModel:
    def __init__(self, mu_max=0.5, Ks=0.01, Y=0.4):
        self.mu_max = mu_max
        self.Ks = Ks
        self.Y = Y

    def _equations(self, variables, t):
        N, S = variables
        if S < 0: S = 0
        mu = self.mu_max * (S / (self.Ks + S))
        dNdt = mu * N
        dSdt = -(1 / self.Y) * dNdt
        return [dNdt, dSdt]

    def solve(self, N0, S0, t_max, steps=1000):
        self.t = np.linspace(0, t_max, steps)
        y0 = [N0, S0]
        solution = odeint(self._equations, y0, self.t)
        self.N = solution[:, 0]
        self.S = solution[:, 1]
        return self.t, self.N, self.S

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
