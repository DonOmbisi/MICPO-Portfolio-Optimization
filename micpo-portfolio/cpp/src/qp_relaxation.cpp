// src/qp_relaxation.cpp
#include "qp_relaxation.hpp"
#include "node.hpp"   // <-- REQUIRED
#include <Eigen/Sparse>


QPSolution qp_relaxation(
    const Eigen::VectorXd& mu,
    const Eigen::MatrixXd& Sigma,
    int K,
    double U,
    const Node& node) {
int n = mu.size();


// NOTE: For brevity, OSQP matrix assembly is schematic
// In practice, build sparse KKT matrices and warm-start


QPSolution sol;
sol.x = Eigen::VectorXd::Constant(n, 1.0/n);
sol.z = Eigen::VectorXi::Ones(n);
sol.value = sol.x.transpose() * Sigma * sol.x - mu.dot(sol.x);
return sol;
}