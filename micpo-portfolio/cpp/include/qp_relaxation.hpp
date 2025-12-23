#pragma once

#include <Eigen/Dense>

// Forward declaration
class Node;

struct QPSolution {
    double value;
    Eigen::VectorXd x;
    Eigen::VectorXi z;
};

QPSolution qp_relaxation(
    const Eigen::VectorXd& mu,
    const Eigen::MatrixXd& Sigma,
    int K,
    double U,
    const Node& node);

