# QMC
Quine–McCluskey algorithm

The Quine–McCluskey algorithm (or the method of prime implicants) is a method used for minimization of Boolean functions that was developed by Willard V. Quine and extended by Edward J. McCluskey. It is functionally identical to Karnaugh mapping, but the tabular form makes it more efficient for use in computer algorithms, and it also gives a deterministic way to check that the minimal form of a Boolean function has been reached. It is sometimes referred to as the tabulation method.

Although more practical than Karnaugh mapping when dealing with more than four variables, the Quine–McCluskey algorithm also has a limited range of use since the problem it solves is NP-complete. The running time of the Quine–McCluskey algorithm grows exponentially with the number of variables. For a function of n variables the number of prime implicants can be as large as (3^n)ln(n), e.g. for 32 variables there may be over 534 * 10¹² prime implicants. Functions with a large number of variables have to be minimized with potentially non-optimal heuristic methods, of which the Espresso heuristic logic minimizer was the de facto standard in 1995.

Step two of the algorithm amounts to solving the set cover problem;NP-hard instances of this problem may occur in this algorithm step.
