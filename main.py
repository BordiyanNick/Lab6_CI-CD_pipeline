# Модель: Математичне моделювання біологічного росту бактерій (5 семестр)
# Автор: Бордіян Микола Павлович, група AI-231

import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use('Agg') # Обов'язково для Docker! Вимикає спробу відкрити вікно
import matplotlib.pyplot as plt
import sys

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
        try:
            self.t = np.linspace(0, t_max, steps)
            y0 = [N0, S0]
            solution = odeint(self._equations, y0, self.t)
            self.N = solution[:, 0]
            self.S = solution[:, 1]
            return self.t, self.N, self.S
        except Exception as e:
            print(f"Помилка при обчисленні: {e}")
            sys.exit(1)

    def calculate_metrics(self):
        max_n = np.max(self.N)
        td = np.log(2) / self.mu_max
        idx_stat = np.where(self.S < 0.01 * np.max(self.S))[0]
        t_stat = self.t[idx_stat[0]] if len(idx_stat) > 0 else None
        return max_n, td, t_stat

    def plot(self):
        max_n, td, t_stat = self.calculate_metrics()
        fig, ax1 = plt.subplots(figsize=(12, 7))

        ax1.set_xlabel('Час (години)', fontsize=12)
        ax1.set_ylabel('Біомаса бактерій (N, г/л)', color='darkgreen', fontsize=12)
        line1, = ax1.plot(self.t, self.N, color='darkgreen', linewidth=3, label='Чисельність бактерій (N)')
        ax1.fill_between(self.t, self.N, color='green', alpha=0.1)
        ax1.tick_params(axis='y', labelcolor='darkgreen')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Концентрація субстрату (S, г/л)', color='darkred', fontsize=12)
        line2, = ax2.plot(self.t, self.S, color='darkred', linestyle='--', linewidth=2, label='Субстрат (S)')
        ax2.tick_params(axis='y', labelcolor='darkred')

        if t_stat:
            ax1.axvline(x=t_stat, color='gray', linestyle=':', label='Початок стац. фази')

        plt.title('Моделювання росту бактерій (Модель Моно)', fontsize=14)
        ax1.grid(True, which='both', linestyle='--', alpha=0.5)
        
        lines = [line1, line2]
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='center right')

        info_text = f'Max N: {max_n:.2f} г/л\nЧас подвоєння: {td:.2f} год'
        plt.gcf().text(0.15, 0.8, info_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

        plt.tight_layout()
        plt.savefig("bacterial_growth_detailed.png", dpi=300)
        print(f"Аналіз завершено. Максимальна біомаса: {max_n:.2f}")
        print("Графік успішно збережено у файл 'bacterial_growth_detailed.png' всередині контейнера.")

if __name__ == '__main__':
    growth_sim = BacteriaGrowthModel(mu_max=0.5, Ks=0.01, Y=0.4)
    growth_sim.solve(N0=0.05, S0=2.0, t_max=30)
    growth_sim.plot()
