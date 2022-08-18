INCLUDE_DIRECTORIES(/usr/local/include/hello)
INCLUDE_DIRECTORIES(/usr/include/hello)
add_executable(hello main.cpp)
TARGET_LINK_LIBRARIES(hello libhello.a)