#pragma once

#ifdef WIN32
#define say_EXPORT __declspec(dllexport)
#else
#define say_EXPORT
#endif

#include "Eigen/Dense"

say_EXPORT void say(const Eigen::Vector3d v);
