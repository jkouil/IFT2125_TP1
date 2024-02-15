cmake_minimum_required(VERSION 3.22)
project(IFT2125_TP1)

set(CMAKE_CXX_STANDARD 14)

include_directories("Q2 nth prime")

add_executable(IFT2125_TP1
        "Q2 nth prime/nth_prime.cpp"
        "Q2 nth prime/PrimeCalculator.cpp"
        "Q2 nth prime/PrimeCalculator.h")
