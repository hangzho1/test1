# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sfdev/hangz/cmkehz/cmake02

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sfdev/hangz/cmkehz/cmake02/build

# Include any dependencies generated for this target.
include bin/CMakeFiles/hello.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include bin/CMakeFiles/hello.dir/compiler_depend.make

# Include the progress variables for this target.
include bin/CMakeFiles/hello.dir/progress.make

# Include the compile flags for this target's objects.
include bin/CMakeFiles/hello.dir/flags.make

bin/CMakeFiles/hello.dir/hello.o: bin/CMakeFiles/hello.dir/flags.make
bin/CMakeFiles/hello.dir/hello.o: ../lib/hello.cpp
bin/CMakeFiles/hello.dir/hello.o: bin/CMakeFiles/hello.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sfdev/hangz/cmkehz/cmake02/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object bin/CMakeFiles/hello.dir/hello.o"
	cd /home/sfdev/hangz/cmkehz/cmake02/build/bin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT bin/CMakeFiles/hello.dir/hello.o -MF CMakeFiles/hello.dir/hello.o.d -o CMakeFiles/hello.dir/hello.o -c /home/sfdev/hangz/cmkehz/cmake02/lib/hello.cpp

bin/CMakeFiles/hello.dir/hello.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/hello.dir/hello.i"
	cd /home/sfdev/hangz/cmkehz/cmake02/build/bin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sfdev/hangz/cmkehz/cmake02/lib/hello.cpp > CMakeFiles/hello.dir/hello.i

bin/CMakeFiles/hello.dir/hello.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/hello.dir/hello.s"
	cd /home/sfdev/hangz/cmkehz/cmake02/build/bin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sfdev/hangz/cmkehz/cmake02/lib/hello.cpp -o CMakeFiles/hello.dir/hello.s

# Object files for target hello
hello_OBJECTS = \
"CMakeFiles/hello.dir/hello.o"

# External object files for target hello
hello_EXTERNAL_OBJECTS =

bin/libhello.so: bin/CMakeFiles/hello.dir/hello.o
bin/libhello.so: bin/CMakeFiles/hello.dir/build.make
bin/libhello.so: bin/CMakeFiles/hello.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sfdev/hangz/cmkehz/cmake02/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libhello.so"
	cd /home/sfdev/hangz/cmkehz/cmake02/build/bin && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hello.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
bin/CMakeFiles/hello.dir/build: bin/libhello.so
.PHONY : bin/CMakeFiles/hello.dir/build

bin/CMakeFiles/hello.dir/clean:
	cd /home/sfdev/hangz/cmkehz/cmake02/build/bin && $(CMAKE_COMMAND) -P CMakeFiles/hello.dir/cmake_clean.cmake
.PHONY : bin/CMakeFiles/hello.dir/clean

bin/CMakeFiles/hello.dir/depend:
	cd /home/sfdev/hangz/cmkehz/cmake02/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sfdev/hangz/cmkehz/cmake02 /home/sfdev/hangz/cmkehz/cmake02/lib /home/sfdev/hangz/cmkehz/cmake02/build /home/sfdev/hangz/cmkehz/cmake02/build/bin /home/sfdev/hangz/cmkehz/cmake02/build/bin/CMakeFiles/hello.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : bin/CMakeFiles/hello.dir/depend

