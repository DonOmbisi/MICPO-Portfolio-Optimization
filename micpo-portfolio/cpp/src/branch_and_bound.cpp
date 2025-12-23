// src/branch_and_bound.cpp
#include "branch_and_bound.hpp"
#include "qp_relaxation.hpp"   // REQUIRED
#include <cmath>


BranchAndBound::BranchAndBound(const PortfolioProblem& p)
: prob(p), best_value(1e18) {}


void BranchAndBound::solve() {
Node root;
branch(root);
}


void BranchAndBound::branch(const Node& node) {
QPSolution sol = solve_qp_relaxation(prob, node);


if (sol.value >= best_value) return;


int n = sol.z.size();
int frac = -1;
for (int i = 0; i < n; ++i) {
if (std::abs(sol.z[i] - std::round(sol.z[i])) > 1e-3) {
frac = i;
break;
}
}


if (frac == -1) {
best_value = sol.value;
best_x = sol.x;
return;
}


for (int v : {0,1}) {
Node child = node;
child.fixed[frac] = v;
branch(child);
}
}