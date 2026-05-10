"""
TASK 6: Writhe Normalization and Jones Polynomial
Helix Topological-PQC Project
Author: Bilal Khan
Date: 2026-05-05

Goal:
Convert Kauffman Bracket into a true topological invariant
using writhe normalization.
"""

import numpy as np


# ==========================
# STEP 1: Compute Writhe
# ==========================
def compute_writhe(braid: list[int]) -> int:
    """
    Writhe = sum of crossing signs
    +1 for positive crossing, -1 for negative crossing
    """
    return sum(1 if x > 0 else -1 for x in braid)


# ==========================
# STEP 2: Normalize Polynomial
# ==========================
def normalized_jones_bracket(braid: list[int], kauffman_poly: dict) -> dict:
    """
    Apply normalization factor: (-A^3)^(-w)

    Math:
    (-A^3)^(-w) = (-1)^(-w) * A^(-3w)
    """
    w = compute_writhe(braid)

    normalized_poly = {}

    exponent_shift = -3 * w
    factor_coeff = (-1) ** (-w)

    for exp, coeff in kauffman_poly.items():
        new_exp = exp + exponent_shift
        new_coeff = coeff * factor_coeff
        normalized_poly[new_exp] = new_coeff

    return normalized_poly


# ==========================
# STEP 3: Evaluate Polynomial
# ==========================
def evaluate(poly_dict: dict, A_value: complex):
    result = 0j
    for exp, coeff in poly_dict.items():
        result += coeff * (A_value ** exp)
    return result


# ==========================
# TEST / USAGE
# ==========================
if __name__ == "__main__":

    print("=== TASK 6: Writhe Normalization ===\n")

    # Trefoil from Task 5
    braid = [1, 1, 1]

    # Your Task 5 result
    kauffman_trefoil = {7: 1, 3: -1, -1: -1}

    # Compute writhe
    w = compute_writhe(braid)
    print(f"Braid: {braid}")
    print(f"Writhe (w): {w}\n")

    # Normalize
    jones_poly = normalized_jones_bracket(braid, kauffman_trefoil)

    print("Normalized Jones-Kauffman Polynomial:")
    for exp in sorted(jones_poly.keys(), reverse=True):
        coeff = jones_poly[exp]
        sign = "+" if coeff > 0 else ""
        print(f"{sign}{coeff} A^{exp}", end=" ")
    print("\n")

    # Evaluate
    A = np.exp(1j * np.pi / 4)
    value = evaluate(jones_poly, A)

    print(f"Evaluated at A = exp(iπ/4): {value.real:.6f} + {value.imag:.6f}i")

    print("\nTask 6 complete.")
    print("Kauffman → Jones normalization achieved.")