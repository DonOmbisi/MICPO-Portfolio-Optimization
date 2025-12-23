// src/osqp_qp.cpp
#include "qp_relaxation.hpp"
#include <osqp.h>
#include <Eigen/Sparse>
#include <vector>

QPSolution solve_qp_relaxation(const PortfolioProblem& prob,
                              const Node& node)
{
    int n = prob.mu.size();
    int N = 2 * n;

    /* ---------------- P matrix ---------------- */
    Eigen::SparseMatrix<double> P(N, N);
    std::vector<Eigen::Triplet<double>> P_triplets;

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (prob.Sigma(i,j) != 0.0)
                P_triplets.emplace_back(i, j, prob.Sigma(i,j));

    P.setFromTriplets(P_triplets.begin(), P_triplets.end());

    /* ---------------- q vector ---------------- */
    Eigen::VectorXd q = Eigen::VectorXd::Zero(N);
    q.head(n) = -prob.mu;

    /* ---------------- A matrix ---------------- */
    std::vector<Eigen::Triplet<double>> A_triplets;
    int row = 0;

    // (1) sum x = 1
    for (int i = 0; i < n; ++i)
        A_triplets.emplace_back(row, i, 1.0);
    row++;

    // (2) x_i - U z_i <= 0
    for (int i = 0; i < n; ++i) {
        A_triplets.emplace_back(row, i, 1.0);
        A_triplets.emplace_back(row, n + i, -prob.U);
        row++;
    }

    // (3) sum z <= K
    for (int i = 0; i < n; ++i)
        A_triplets.emplace_back(row, n + i, 1.0);
    row++;

    Eigen::SparseMatrix<double> A(row, N);
    A.setFromTriplets(A_triplets.begin(), A_triplets.end());

    /* ---------------- bounds ---------------- */
    Eigen::VectorXd l = Eigen::VectorXd::Constant(row, -OSQP_INFTY);
    Eigen::VectorXd u = Eigen::VectorXd::Constant(row,  OSQP_INFTY);

    l(0) = u(0) = 1.0;          // sum x = 1
    for (int i = 1; i <= n; ++i)
        u(i) = 0.0;             // x_i - U z_i <= 0
    u(row - 1) = prob.K;        // sum z <= K

    /* ---------------- OSQP setup ---------------- */
    OSQPSettings* settings = (OSQPSettings*)c_malloc(sizeof(OSQPSettings));
    osqp_set_default_settings(settings);
    settings->verbose = false;
    settings->warm_start = true;
    settings->polish = false;

    OSQPData* data = (OSQPData*)c_malloc(sizeof(OSQPData));
    data->n = N;
    data->m = row;
    data->P = csc_matrix(P.rows(), P.cols(), P.nonZeros(),
                          (c_float*)P.valuePtr(),
                          (c_int*)P.innerIndexPtr(),
                          (c_int*)P.outerIndexPtr());
    data->A = csc_matrix(A.rows(), A.cols(), A.nonZeros(),
                          (c_float*)A.valuePtr(),
                          (c_int*)A.innerIndexPtr(),
                          (c_int*)A.outerIndexPtr());
    data->q = (c_float*)q.data();
    data->l = (c_float*)l.data();
    data->u = (c_float*)u.data();

    OSQPWorkspace* work = osqp_setup(data, settings);
    osqp_solve(work);

    /* ---------------- extract solution ---------------- */
    QPSolution sol;
    sol.x = Eigen::VectorXd::Map(work->solution->x, n);
    sol.z = Eigen::VectorXd::Map(work->solution->x + n, n);
    sol.value = work->info->obj_val;

    osqp_cleanup(work);
    c_free(data);
    c_free(settings);

    return sol;
}
