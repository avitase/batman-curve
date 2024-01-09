import matplotlib.pyplot as plt
import numpy as np

from batman_curve import batman

plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "sans-serif",
        "figure.figsize": (4, 3),
        "figure.dpi": 140,
    }
)

x = np.linspace(-7, 7, 300)
upper, lower = batman(x)

fig, ax = plt.subplots()
ax.plot(x, upper)
ax.plot(x, lower)

ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

fig.tight_layout()
fig.savefig("batman.png")
