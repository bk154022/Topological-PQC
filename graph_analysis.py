import numpy as np
import matplotlib.pyplot as plt
from braid_word import compute_braid_word
from trace_invariant import trace_invariant
import os

# -----------------------------
# Create output folder
# -----------------------------
save_dir = "graphs"
os.makedirs(save_dir, exist_ok=True)

# -----------------------------
# Braid words
# -----------------------------
words = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 2, 1, 2],
    [1, -1],
    [1, 1, 2]
]

labels = []
magnitudes = []

for w in words:
    tr, mag = trace_invariant(w)
    labels.append(str(w))
    magnitudes.append(mag)

# -----------------------------
# 1. 2D BAR GRAPH
# -----------------------------
plt.figure()
plt.bar(labels, magnitudes)
plt.xlabel("Braid Words")
plt.ylabel("Trace Magnitude")
plt.title("Braid Trace Magnitudes (2D)")
plt.xticks(rotation=45)
plt.tight_layout()

file1 = os.path.join(save_dir, "braid_trace_2D.png")
plt.savefig(file1)
plt.show()

print(f"Saved: {file1}")

# -----------------------------
# 2. 3D STYLE PLOT
# -----------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(len(words))
y = magnitudes
z = np.zeros(len(words))

ax.plot(x, y, z, marker='o')

ax.set_xlabel("Index")
ax.set_ylabel("Magnitude")
ax.set_zlabel("Z-axis")
ax.set_title("Braid Trace 3D View")

file2 = os.path.join(save_dir, "braid_trace_3D.png")
plt.savefig(file2)

plt.show()

print(f"Saved: {file2}")