import numpy as np
import matplotlib.pyplot as plt

# --- x values from -6 to 6 ---
x = np.linspace(-6, 6, 500)

# --- Multiple distributions: (mean, std_dev, label) ---
distributions = [
    (0,   1.0, 'Mean=0, Std=1  (Standard)'),
    (-2,  0.5, 'Mean=-2, Std=0.5 (Narrow)'),
    (2,   1.5, 'Mean=2, Std=1.5 (Wide)'),
    (0,   2.0, 'Mean=0, Std=2  (Very Wide)'),
]

# --- Green shades for each curve ---
colors = ['#00c853', '#69f0ae', '#1b5e20', '#b9f6ca']

# --- Plot ---
plt.figure(figsize=(10, 6))

for (mean, std, label), color in zip(distributions, colors):
    # Normal distribution formula
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)

    plt.plot(x, y, color=color, linewidth=2.5, label=label)
    plt.fill_between(x, y, alpha=0.15, color=color)

# --- Styling ---
plt.title('Bell Curves - Normal Distribution (Multiple)', fontsize=16)
plt.xlabel('x values', fontsize=13)
plt.ylabel('Probability Density', fontsize=13)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()
