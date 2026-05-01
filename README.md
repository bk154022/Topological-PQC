# Braid-to-Matrix Engine (Topological PQC Prototype)

## Objective
Convert braid words into unitary matrices and study trace invariants.

## Current Work
- Implemented σ₁ and σ₂ generators
- Computed braid word matrices
- Verified trace invariance for trefoil knot

## Next Steps
- Introduce θ = γ log(p)
- Explore parameterized invariants
- Move toward Kauffman bracket / Jones polynomial

## Author
Bilal Khan



1. Generator Matrices Output

When running generators.py, we get the braid matrices σ₁ and σ₂:

[[ 0.5      +0.j -0.8660254+0.j  0.       +0.j  0.       +0.j]
 [ 0.8660254+0.j  0.5      +0.j  0.       +0.j  0.       +0.j]
 [ 0.       +0.j  0.       +0.j  1.       +0.j  0.       +0.j]
 [ 0.       +0.j  0.       +0.j  0.       +0.j  1.       +0.j]]
[[ 1.       +0.j  0.       +0.j  0.       +0.j  0.       +0.j]
 [ 0.       +0.j  0.5      +0.j -0.8660254+0.j  0.       +0.j]
 [ 0.       +0.j  0.8660254+0.j  0.5      +0.j  0.       +0.j]
 [ 0.       +0.j  0.       +0.j  0.       +0.j  1.       +0.j]]
Simple meaning:

These matrices represent braid crossings as rotations.



3. Braid Word Output

For trefoil knot [1, 2, 1]:

Final matrix for trefoil (first 4x4):
[[ 0.5      +0.j -0.8660254+0.j  0.       +0.j  0.       +0.j]
 [ 0.       +0.j  0.       +0.j  1.       +0.j  0.       +0.j]
 [ 0.       +0.j  0.       +0.j  0.       +0.j  1.       +0.j]]
Meaning:

A braid word is converted into a final matrix using multiplication.



4. Trace Results
First run:
Trace of trefoil braid: 7
Magnitude: 7.000000
Later run (after parameter update):
Trace of trefoil braid: 7.7190269566
Magnitude: 7.719027




5. Invariance Test
Same knot, different word:
[1,2,1] and [2,1,2]

Magnitudes match: True
Meaning:

Different braid representation gives same invariant value.




6. Experiment Results
[1, 2, 1] → 7.719
[2, 1, 2] → 7.719
[1, 2, 1, 2] → 7.719
[1, -1] → 7.719
[1, 1, 2] → 7.719
Observation:

All tested braid words produced the same trace magnitude in current model.