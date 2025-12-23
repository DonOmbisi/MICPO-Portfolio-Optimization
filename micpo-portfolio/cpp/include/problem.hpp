// include/problem.hpp
#pragma once
#include <Eigen/Dense>


struct PortfolioProblem {
Eigen::VectorXd mu;
Eigen::MatrixXd Sigma;
int K;
double U;
};