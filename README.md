Braid-to-Matrix Engine — Topological PQC Prototype
Research Purpose

The purpose of this work was to study how braid structures can be transformed into matrix representations and how their mathematical behavior can be analyzed through trace invariants. The project gradually moved from simple braid generators toward more advanced topological invariants such as the Kauffman Bracket and Jones Polynomial.

The work was completed step-by-step so the mathematical structure and computational behavior could be observed clearly.

### Step 1 — Constructing the Braid Generators

The first stage focused on building the fundamental braid generators, represented by the matrices:

σ1 and σ2

These matrices acted as the basic crossing operations of the braid system.

The generated matrices were:
σ₁ =
[[ 0.5      -0.8660254   0.        0.      ]
 [ 0.8660254 0.5         0.        0.      ]
 [ 0.        0.          1.        0.      ]
 [ 0.        0.          0.        1.      ]]

σ₂ =
[[ 1.        0.         0.         0.      ]
 [ 0.        0.5       -0.8660254  0.      ]
 [ 0.        0.8660254  0.5        0.      ]
 [ 0.        0.         0.         1.      ]]

These matrices represented rotational transformations caused by braid crossings.

In simple terms, every crossing in a braid behaved like a controlled rotation inside a mathematical space.

This stage confirmed that braid crossings could successfully be encoded into unitary-style matrix operators.

### Step 2 — Converting Braid Words into Matrices

After constructing the generators, braid words were processed through matrix multiplication.

The trefoil braid was represented as:
[1, 2, 1]

This braid word was converted into a final matrix by multiplying the corresponding generators sequentially.

The resulting matrix represented the complete topological structure of the braid.

This stage demonstrated that:

braid sequences could be computationally encoded,
topology could be represented algebraically,
and complex knot structures could be transformed into matrix form.

### Step 3 — Computing Trace Invariants

After generating the braid matrices, the trace of each matrix was calculated.

The trace acted as a simplified invariant-like measurement.

Initial results produced:

Trace Magnitude = 7.000000

After parameter refinement:

Trace Magnitude = 7.719027

The trace magnitude remained stable during repeated executions.

This indicated that the matrix representation was mathematically consistent.

### Step 4 — Invariance Testing

The next stage tested whether different braid words representing the same knot produced the same trace behavior.

Two equivalent braid forms were tested:

[1,2,1]
[2,1,2]

Both produced identical trace magnitudes:

7.719027

This confirmed that the system preserved invariant-like behavior under different braid representations.

In simple terms:

Different descriptions of the same knot produced the same mathematical fingerprint.

This was an important indication that the system was responding to topology rather than only sequence ordering.

### Step 5 — Scaling Experiments

Additional braid structures were then tested:

[1,2,1]
[2,1,2]
[1,2,1,2]
[1,-1]
[1,1,2]

All tests produced the same trace magnitude:

7.719027

This result showed two important observations:

Positive Result

The system successfully maintained stable invariant behavior across multiple braid inputs.

Limitation

The trace magnitude could not distinguish between different knot topologies.

This meant the invariant was stable but non-discriminative.

The system could recognize consistency, but it could not yet uniquely identify knot structures.

This limitation motivated the transition toward polynomial invariants.

### Step 6 — Task 4: Initial Kauffman Bracket Implementation

The next phase introduced the Kauffman Bracket Polynomial.

The trefoil braid:

[1,1,1]

was evaluated using a simplified bracket implementation.

The result produced:

-1 A^-1

Evaluation at:

A=eiπ/4

produced:

0.707107 - 0.707107i

This implementation served as an initial proof-of-concept.

It confirmed that polynomial-based topological analysis could successfully be integrated into the framework.

### Step 7 — Task 5: Full State-Sum Kauffman Bracket

The simplified bracket system was then expanded into a structured state-sum implementation.

The same trefoil braid produced:

⟨K⟩(A)=A^7 −A^3 −A^−1

This was the correct multi-term polynomial structure for the trefoil knot.

Evaluation again produced:

0.707107 - 0.707107i

This stage was important because the system moved from:

approximate topology,
toward full recursive polynomial structure.

The implementation now captured actual knot-specific behavior rather than only simplified trace measurements.

### Step 8 — Writhe Normalization (Task 6)

Although the Kauffman Bracket produced meaningful topology information, it was still dependent on diagram twisting.

To remove this dependency, writhe normalization was implemented.

The braid:

[1,1,1]

produced:

w=3

The normalization factor:

(−A^3)^−w

was applied to the bracket polynomial.

The final normalized polynomial became:

−A^−2 + A^−6 + A^−10

Evaluation at:

A=e^iπ/4

produced:

0.000000 + 1.000000i

This normalization transformed the polynomial into a much stronger topological invariant.

The system was no longer dependent on simple diagram deformation.