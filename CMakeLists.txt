cmake_minimum_required(VERSION 3.16...3.31)
project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION})

message(STATUS "clang-apply-replacements wheel version: ${SKBUILD_PROJECT_VERSION}")
string(REGEX MATCH "^([0-9]+)\.([0-9]+)\.([0-9]+)" LLVM_VERSION "${SKBUILD_PROJECT_VERSION}")
set(LLVM_VERSION_MAJOR ${CMAKE_MATCH_1}) # https://cmake.org/cmake/help/latest/variable/CMAKE_MATCH_n.html
message(STATUS "LLVM version: ${LLVM_VERSION}")

# Define a build rule for clang-apply-replacements
# LLVM releases before 12.0.0 use a filename without ".src" (e.g., llvm-project-11.0.0.tar.xz),
# while LLVM >= 12.0.0 use llvm-project-X.Y.Z.src.tar.xz.
if(LLVM_VERSION_MAJOR LESS 12)
  set(LLVM_DOWNLOAD_URL "https://github.com/llvm/llvm-project/releases/download/llvmorg-${LLVM_VERSION}/llvm-project-${LLVM_VERSION}.tar.xz")
else()
  set(LLVM_DOWNLOAD_URL "https://github.com/llvm/llvm-project/releases/download/llvmorg-${LLVM_VERSION}/llvm-project-${LLVM_VERSION}.src.tar.xz")
endif()
include(ExternalProject)
ExternalProject_add(build-clang-apply-replacements
  URL "${LLVM_DOWNLOAD_URL}"
  SOURCE_SUBDIR llvm
  SOURCE_DIR ${CMAKE_BINARY_DIR}/llvm-project
  BINARY_DIR ${CMAKE_BINARY_DIR}/llvm
  UPDATE_COMMAND ""
  INSTALL_COMMAND ""
  USES_TERMINAL_DOWNLOAD 1
  USES_TERMINAL_CONFIGURE 1
  USES_TERMINAL_BUILD 1
  CMAKE_ARGS -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DLLVM_ENABLE_ZSTD=OFF -DLLVM_ENABLE_PROJECTS=clang$<SEMICOLON>clang-tools-extra
  BUILD_COMMAND ${CMAKE_COMMAND} --build . --target clang-apply-replacements
)

set(config-subfolder "")
if(CMAKE_GENERATOR MATCHES "Visual Studio")
  set(config-subfolder "Release")
endif()
set(clang-apply-replacements-executable ${CMAKE_BINARY_DIR}/llvm/${config-subfolder}/bin/clang-apply-replacements${CMAKE_EXECUTABLE_SUFFIX})

# Reduce the size of the executable by executing strip if it is present on the system
find_program(STRIP_EXECUTABLE strip)
if(STRIP_EXECUTABLE)
  add_custom_target(
    strip-clang-apply-replacements
    ALL
    COMMAND ${STRIP_EXECUTABLE} ${clang-apply-replacements-executable}
    COMMENT "Stripping clang-apply-replacements executable for size reduction"
  )
  add_dependencies(strip-clang-apply-replacements build-clang-apply-replacements)
endif()

# Define an installation rule that copies the executable to our Python package
install(
  PROGRAMS
    ${clang-apply-replacements-executable}
  DESTINATION clang_apply_replacements/data/bin
)

install(
  DIRECTORY
    ${CMAKE_BINARY_DIR}/llvm/lib/clang/${LLVM_VERSION_MAJOR}/include
  DESTINATION clang_apply_replacements/data/lib/clang/${LLVM_VERSION_MAJOR}
)
