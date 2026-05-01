import numpy as np
from generators import get_braid_generators
def compute_braid_word(word_indices):
  s1, s2 = get_braid_generators()
  # Map index -> matrix (positive for forward, negative for inverse)
  generators = {
   1: s1,
   -1: np.linalg.inv(s1),
   2: s2,
   -2: np.linalg.inv(s2)
   }
  M = np.eye(8, dtype=complex)
  for idx in word_indices:
    M = M @ generators[idx]
    return M
if __name__ == "__main__":
 trefoil = [1, 2, 1, 2]
 M = compute_braid_word(trefoil)
 print("Final matrix for trefoil (first 4x4):\n", M[:4, :4])