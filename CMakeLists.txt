cmake_minimum_required(VERSION 3.22)
project(devoir1_IFT2125)

set(CMAKE_CXX_STANDARD 14)

include_directories("Q2 nth prime")

add_executable(devoir1_IFT2125
        "Q2 nth prime/nth_prime.cpp"
        "Q2 nth prime/PrimeCalculator.cpp"
        "Q2 nth prime/PrimeCalculator.h")
