Electric Field Practice App — Version 2 Specification
Overview

This document specifies Version 2 of the Electric Field Practice App.

Changes introduced in V2:

Expand the coordinate grid range from [-2, 2] to [-4, 4]

Add grading for:

Electric field magnitude 
∣
𝐸
⃗
∣
∣
E
∣

Electric field angle 
𝜃
θ

All four answers are required:

𝐸
𝑥
E
x
	​


𝐸
𝑦
E
y
	​


∣
𝐸
⃗
∣
∣
E
∣

𝜃
θ

Grading tolerance:

3% relative tolerance for components and magnitude

±3° tolerance for angle

If a student leaves a field blank, that part receives 0 credit

Preserve all existing behavior unless explicitly modified here.

1. Physics Conventions
1.1 Grid System

Coordinates are integer grid points:

𝑥
,
𝑦
∈
{
−
4
,
−
3
,
−
2
,
−
1
,
0
,
1
,
2
,
3
,
4
}
x,y∈{−4,−3,−2,−1,0,1,2,3,4}

Grid spacing:

1
 grid unit
=
0.10
 m
1 grid unit=0.10 m

Convert to meters:

𝑥
𝑚
=
𝑥
⋅
0.10
x
m
	​

=x⋅0.10
𝑦
𝑚
=
𝑦
⋅
0.10
y
m
	​

=y⋅0.10
1.2 Charge Units

Charges are displayed in nC

Convert to Coulombs:

𝑞
𝐶
=
𝑞
𝑛
𝐶
⋅
10
−
9
q
C
	​

=q
nC
	​

⋅10
−9
1.3 Electric Field Calculation

Field at target charge Q1 due to Q2, Q3, Q4 only.

For each source charge 
𝑖
i:

𝑟
⃗
𝑖
=
(
𝑥
1
−
𝑥
𝑖
,
  
𝑦
1
−
𝑦
𝑖
)
r
i
	​

=(x
1
	​

−x
i
	​

,y
1
	​

−y
i
	​

)
𝑟
𝑖
=
∣
𝑟
⃗
𝑖
∣
r
i
	​

=∣
r
i
	​

∣
𝐸
⃗
𝑖
=
𝑘
𝑞
𝑖
𝑟
𝑖
3
𝑟
⃗
𝑖
E
i
	​

=k
r
i
3
	​

q
i
	​

	​

r
i
	​


Total field:

𝐸
⃗
=
∑
𝑖
𝐸
⃗
𝑖
E
=
i
∑
	​

E
i
	​


Where:

𝑘
=
8.9875517923
×
10
9
 
N
\cdotp
m
2
/
C
2
k=8.9875517923×10
9
N\cdotpm
2
/C
2
2. Derived Quantities
2.1 Magnitude
∣
𝐸
⃗
∣
=
𝐸
𝑥
2
+
𝐸
𝑦
2
∣
E
∣=
E
x
2
	​

+E
y
2
	​

	​

2.2 Angle Definition

Angle must use:

𝜃
=
a
t
a
n
2
(
𝐸
𝑦
,
𝐸
𝑥
)
θ=atan2(E
y
	​

,E
x
	​

)

Measured from +x axis

Positive counterclockwise

In degrees

Canonical range: (-180°, +180°]

Students may enter any equivalent angle (e.g. 270°, -90°, etc.).
Grading must use wrap-safe comparison.

3. Problem Generation Rules
3.1 Coordinate Sampling

Sample integer grid coordinates from [-4, 4]

All four charges must have distinct coordinates

3.2 Separation Constraint

No two charges may occupy the same coordinate

Ensure no source charge is at zero distance from target

3.3 Determinism

Problem must be reproducible from seed

All random choices must derive from seed

4. Grading Rules
4.1 Required Fields

All four fields are required and graded independently:

Quantity	Points

𝐸
𝑥
E
x
	​

	1

𝐸
𝑦
E
y
	​

	1
(	\vec{E}

𝜃
θ	1

Total score: 0–4.

If a field is blank:

Store as NULL

Mark incorrect

Award 0 points for that part

4.2 Relative Tolerance (3%)

For expected value 
𝑇
T and student value 
𝑆
S:

If 
𝑇
≠
0
T

=0:

percent error
=
∣
𝑆
−
𝑇
𝑇
∣
×
100
percent error=
	​

T
S−T
	​

	​

×100

Correct if:

percent error
≤
3
percent error≤3

If 
𝑇
=
0
T=0:

Use absolute tolerance:

∣
𝑆
−
𝑇
∣
≤
1.0
 N/C
∣S−T∣≤1.0 N/C
4.3 Angle Grading (±3°)

Let:

𝜃
𝑡
θ
t
	​

 = true angle

𝜃
𝑠
θ
s
	​

 = student angle

Compute:

diff = abs(theta_s - theta_t) % 360
delta = min(diff, 360 - diff)

Correct if:

delta <= 3
5. Database Changes

If attempts are stored, add columns:

expected_emag (float)

expected_theta (float)

submitted_emag (float, nullable)

submitted_theta (float, nullable)

emag_correct (bool)

theta_correct (bool)

theta_error_deg (float, optional)

grading_version (string, default = "v2")

Create and apply Alembic migration.

6. UI Updates

Update displayed coordinate range to [-4, 4]

Add input fields:

|E| (N/C)

θ (degrees)

Keep layout consistent with existing design

7. Testing Requirements

Add tests for:

Correct magnitude computation

Correct atan2 angle behavior in all quadrants

Angle wrap cases:

179° vs -179°

5° vs 365°

3% tolerance behavior

Deterministic seed generation

8. Acceptance Criteria

The app must:

Generate coordinates in [-4, 4]

Compute Ex, Ey, |E|, θ correctly

Grade using 3% and ±3°

Assign 0 credit to blank fields

Successfully deploy on Render

Maintain compatibility with existing seeds where applicable

End of Specification
