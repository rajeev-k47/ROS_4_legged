# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_lg-robot_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED lg-robot_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(lg-robot_FOUND FALSE)
  elseif(NOT lg-robot_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(lg-robot_FOUND FALSE)
  endif()
  return()
endif()
set(_lg-robot_CONFIG_INCLUDED TRUE)

# output package information
if(NOT lg-robot_FIND_QUIETLY)
  message(STATUS "Found lg-robot: 0.0.0 (${lg-robot_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'lg-robot' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${lg-robot_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(lg-robot_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${lg-robot_DIR}/${_extra}")
endforeach()
