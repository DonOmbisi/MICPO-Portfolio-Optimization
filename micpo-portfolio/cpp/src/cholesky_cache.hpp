// include/cholesky_cache.hpp
#pragma once
#include <Eigen/Dense>
#include <unordered_map>


class CholeskyCache {
public:
const Eigen::MatrixXd& get(const Eigen::MatrixXd& Sigma);


private:
std::unordered_map<size_t, Eigen::MatrixXd> cache;
};