cmake_minimum_required(VERSION 3.10)
project(micpo)


find_package(Eigen3 REQUIRED)


add_executable(micpo
src/main.cpp
src/branch_and_bound.cpp
src/qp_relaxation.cpp
src/heuristics.cpp)


target_include_directories(micpo PRIVATE include)
target_link_libraries(micpo Eigen3::Eigen)