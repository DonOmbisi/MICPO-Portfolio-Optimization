// src/heuristics.cpp
#include "heuristics.hpp"
#include <vector>
#include <algorithm>


Eigen::VectorXd greedy_heuristic(const Eigen::VectorXd& mu,
const Eigen::MatrixXd& Sigma,
int K) {
int n = mu.size();
std::vector<std::pair<double,int>> score;


for (int i = 0; i < n; ++i) {
score.push_back({mu[i] / std::sqrt(Sigma(i,i)), i});
}


std::sort(score.begin(), score.end(), std::greater<>());


Eigen::VectorXd x = Eigen::VectorXd::Zero(n);
for (int i = 0; i < K; ++i) {
x[score[i].second] = 1.0 / K;
}
return x;
}