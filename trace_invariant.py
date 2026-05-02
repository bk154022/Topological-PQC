import numpy as np
from braid_word import compute_braid_word
def trace_invariant(word):
  M = compute_braid_word(word)
  trace = np.trace(M)
  magnitude = abs(trace)
  return trace, magnitude

if __name__ == "__main__":
 trefoil = [1, 2, 1]
 tr, mag = trace_invariant(trefoil)
 print(f"Trace of trefoil braid: {tr}")
 print(f"Magnitude of trace: {mag:.6f}")
 # Bonus: different representation of the same knot
 other_word = [2, 1, 2] # also a trefoil
 tr2, mag2 = trace_invariant(other_word)
 print(f"\nSame knot, different word: trace = {tr2}, magnitude = {mag2:.6f}")
 print("Magnitudes match:", np.isclose(mag, mag2))

# ---- Cinquefoil Test ----
cinquefoil = [1, 1, 1, 1, 1]
tr_c, mag_c = trace_invariant(cinquefoil)

print("\nCinquefoil results:")
print(f"Trace: {tr_c}")
print(f"Magnitude: {mag_c:.6f}")
 
print("\n--- Experiments ---")

words = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 2, 1, 2],
    [1, -1],
    [1, 1, 2]
]

for w in words:
    tr, mag = trace_invariant(w)
    print(w, "→", round(mag, 4))


print("\n--- Scaling Test ---")

tests = {
    "Trefoil": [1,2,1],
    "Cinquefoil": [1,1,1,1,1]
}

for name, word in tests.items():
    tr, mag = trace_invariant(word)
    print(name, "→", round(mag, 6))