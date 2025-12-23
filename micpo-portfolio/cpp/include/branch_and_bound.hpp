// include/branch_and_bound.hpp
#pragma once
#include "problem.hpp"
#include "node.hpp"
#include "qp_relaxation.hpp"


class BranchAndBound {
public:
BranchAndBound(const PortfolioProblem& p);
void solve();


double best_value;
Eigen::VectorXd best_x;


private:
PortfolioProblem prob;
void branch(const Node& node);
};