// src/main.cpp
#include "branch_and_bound.hpp"
#include <iostream>


int main() {
int n = 500;
PortfolioProblem prob;
prob.mu = Eigen::VectorXd::Random(n);
prob.Sigma = Eigen::MatrixXd::Identity(n,n);
prob.K = 20;
prob.U = 0.1;


BranchAndBound solver(prob);
solver.solve();


std::cout << "Best value: " << solver.best_value << std::endl;
}