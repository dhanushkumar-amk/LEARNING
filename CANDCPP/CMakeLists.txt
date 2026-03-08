cmake_minimum_required(VERSION 4.1)
project(CANDCPP C)

set(CMAKE_C_STANDARD 11)

add_executable(CANDCPP main.c
        hello.c
        helloWorld.c)
