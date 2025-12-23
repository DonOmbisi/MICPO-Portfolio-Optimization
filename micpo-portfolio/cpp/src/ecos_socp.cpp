// src/ecos_socp.cpp
#include <ecos.h>
#include "problem.hpp"

void solve_socp_ecos(const PortfolioProblem& prob)
{
    // Dimensions
    int n = prob.mu.size();
    int k = prob.B.cols();

    // Number of variables:
    // x (n), z (n), t_f, t_d
    int N = 2*n + 2;

    // Number of equality constraints (budget)
    int p = 1;

    // Number of inequality rows (linear + SOC)
    int m = /* computed from cones */;

    /* ---------------- Cones ---------------- */
    cone* cones = (cone*)malloc(sizeof(cone));
    cones->l = 2*n;          // linear constraints
    cones->qsize = 2;
    cones->q = (int*)malloc(2 * sizeof(int));
    cones->q[0] = k + 1;     // factor risk SOC
    cones->q[1] = n + 1;     // idiosyncratic SOC

    /* ---------------- Matrices ---------------- */
    // A x = b (budget)
    // G x + s = h (linear + SOC)

    // Build sparse matrices in CSC form
    // (Omitted here for clarity; follows ECOS documentation exactly)

    pwork* work = ECOS_setup(
        N, m, p,
        cones->l, cones->qsize,
        Gx, Gi, Gp,
        Ax, Ai, Ap,
        c, h, b,
        cones
    );

    ECOS_solve(work);

    // Extract solution
    const double* sol = work->x;

    ECOS_cleanup(work, 0);
}
