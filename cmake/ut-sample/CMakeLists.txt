cmake_minimum_required (VERSION 3.6)

add_executable(example TestSample)
target_link_libraries(example gtest_main)
add_test(NAME example_test COMMAND example)

