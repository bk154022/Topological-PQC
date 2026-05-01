import numpy as np
def get_braid_generators(dim=8):
 # Identity matrix
 I = np.eye(dim, dtype=complex)

 # Phase-lock angle (related to γ = 1/3)
 gamma = 1/3
 p = 5
 theta = gamma * np.log(p)
 #theta = np.pi / 3
 c = np.cos(theta)
 s = np.sin(theta)

 # 2x2 rotation block for a single crossing
 rotation = np.array([[c, -s], [s, c]], dtype=complex)

 # σ₁ acts on strands 1 and 2 (indices 0 and 1)
 sigma1 = np.copy(I)
 sigma1[0:2, 0:2] = rotation

 # σ₂ acts on strands 2 and 3 (indices 1 and 2)
 sigma2 = np.copy(I)
 sigma2[1:3, 1:3] = rotation

 return sigma1, sigma2
if __name__ == "__main__":
 s1, s2 = get_braid_generators()
 print("σ₁ (first 4x4 corner):\n", s1[:4, :4])
 print("\nσ₂ (first 4x4 corner):\n", s2[:4, :4])