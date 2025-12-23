// include/heuristics.hpp
#pragma once
#include <Eigen/Dense>


Eigen::VectorXd greedy_heuristic(const Eigen::VectorXd& mu,
const Eigen::MatrixXd& Sigma,
int K);