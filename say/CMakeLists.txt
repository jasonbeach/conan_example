cmake_minimum_required(VERSION 3.15)
project(say VERSION 1.0.0)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

# project wide setup
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)
set(CMAKE_EXPORT_COMPILE_COMMANDS YES)
set(CMAKE_INSTALL_MESSAGE LAZY)

set(PROJECT_INSTALL_BIN_DIR ${CMAKE_INSTALL_BINDIR})
set(PROJECT_INSTALL_LIB_DIR ${CMAKE_INSTALL_LIBDIR})
set(PROJECT_INSTALL_CONFIG_DIR ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME})
set(PROJECT_INSTALL_INCLUDE_DIR ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME})

find_package(fmt REQUIRED)
find_package(Eigen3 REQUIRED)

add_library(say "")
add_library(ns::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_include_directories(${PROJECT_NAME}
  PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/src>
  $<INSTALL_INTERFACE:${PROJECT_INSTALL_INCLUDE_DIR}/..>
)

add_subdirectory(src/say)

set_target_properties(${PROJECT_NAME}
  PROPERTIES
  SOVERSION ${PROJECT_VERSION_MAJOR}
  VERSION ${PROJECT_VERSION}
)

target_link_libraries(${PROJECT_NAME}
  PUBLIC
    fmt::fmt
    Eigen3::Eigen
)

install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}-targets
  RUNTIME
    DESTINATION ${PROJECT_INSTALL_BIN_DIR}
  ARCHIVE
    DESTINATION ${PROJECT_INSTALL_LIB_DIR}
  LIBRARY
    DESTINATION ${PROJECT_INSTALL_LIB_DIR}
)

# create the file with the exported set of targets in it and install it.
install(
  EXPORT ${PROJECT_NAME}-targets
  FILE ${PROJECT_NAME}-targets.cmake
  NAMESPACE ns::
  DESTINATION ${PROJECT_INSTALL_CONFIG_DIR}
)

# create a version file with compatibility data
write_basic_package_version_file(
  "${PROJECT_BINARY_DIR}/${PROJECT_NAME}-config-version.cmake"
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY SameMajorVersion
)

# create the config file that will find dependencies and load the exported targets for use by a
# downstream project
configure_package_config_file(${CMAKE_CURRENT_LIST_DIR}/${PROJECT_NAME}-config.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}-config.cmake
  INSTALL_DESTINATION ${PROJECT_INSTALL_CONFIG_DIR}
)

install(FILES
  ${PROJECT_BINARY_DIR}/${PROJECT_NAME}-config.cmake
  ${PROJECT_BINARY_DIR}/${PROJECT_NAME}-config-version.cmake
  DESTINATION ${PROJECT_INSTALL_CONFIG_DIR}
)

