# Support-Vector-Machine

You are given two data files - linsep.txt and nonlinsep.txt - each of which contains 100 2D points with
classification labels +1 or -1. The first two columns in each file indicate the 2D coordinates of a point;
and the third column indicates its classification label. The points in linsep.txt are linearly separable.
The points in nonlinsep.txt are not linearly separable in the original space but are linearly separable in
a z-space that uses a simple nonlinear transformation.

a)Find the fattest margin line that separates the points in linsep.txt. Please solve the
problem using a Quadratic Programming solver.

b)Using a kernel function of your choice along with the same Quadratic
Programming solver, find the equation of a curve that separates the points in nonlinsep.txt.
