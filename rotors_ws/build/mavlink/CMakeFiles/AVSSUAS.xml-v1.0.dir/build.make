# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.24

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
CMAKE_COMMAND = /home/varun/bin/cmake

# The command to remove a file.
RM = /home/varun/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/varun/rotors_ws/src/mavlink

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/varun/rotors_ws/build/mavlink

# Utility rule file for AVSSUAS.xml-v1.0.

# Include any custom commands dependencies for this target.
include CMakeFiles/AVSSUAS.xml-v1.0.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/AVSSUAS.xml-v1.0.dir/progress.make

CMakeFiles/AVSSUAS.xml-v1.0: include/v1.0/AVSSUAS/AVSSUAS.h

include/v1.0/AVSSUAS/AVSSUAS.h: /home/varun/rotors_ws/src/mavlink/message_definitions/v1.0/AVSSUAS.xml
include/v1.0/AVSSUAS/AVSSUAS.h: /home/varun/rotors_ws/src/mavlink/message_definitions/v1.0/common.xml
include/v1.0/AVSSUAS/AVSSUAS.h: /home/varun/rotors_ws/src/mavlink/pymavlink/tools/mavgen.py
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/varun/rotors_ws/build/mavlink/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating include/v1.0/AVSSUAS/AVSSUAS.h"
	/usr/bin/env PYTHONPATH="/home/varun/rotors_ws/src/mavlink:/opt/ros/noetic/lib/python3/dist-packages" /usr/bin/python3.8 /home/varun/rotors_ws/src/mavlink/pymavlink/tools/mavgen.py --lang=C --wire-protocol=1.0 --output=include/v1.0 /home/varun/rotors_ws/src/mavlink/message_definitions/v1.0/AVSSUAS.xml

AVSSUAS.xml-v1.0: CMakeFiles/AVSSUAS.xml-v1.0
AVSSUAS.xml-v1.0: include/v1.0/AVSSUAS/AVSSUAS.h
AVSSUAS.xml-v1.0: CMakeFiles/AVSSUAS.xml-v1.0.dir/build.make
.PHONY : AVSSUAS.xml-v1.0

# Rule to build all files generated by this target.
CMakeFiles/AVSSUAS.xml-v1.0.dir/build: AVSSUAS.xml-v1.0
.PHONY : CMakeFiles/AVSSUAS.xml-v1.0.dir/build

CMakeFiles/AVSSUAS.xml-v1.0.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/AVSSUAS.xml-v1.0.dir/cmake_clean.cmake
.PHONY : CMakeFiles/AVSSUAS.xml-v1.0.dir/clean

CMakeFiles/AVSSUAS.xml-v1.0.dir/depend:
	cd /home/varun/rotors_ws/build/mavlink && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/varun/rotors_ws/src/mavlink /home/varun/rotors_ws/src/mavlink /home/varun/rotors_ws/build/mavlink /home/varun/rotors_ws/build/mavlink /home/varun/rotors_ws/build/mavlink/CMakeFiles/AVSSUAS.xml-v1.0.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/AVSSUAS.xml-v1.0.dir/depend

