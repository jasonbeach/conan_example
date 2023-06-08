#include "say/say.h"
#include "fmt/core.h"

void say(const Eigen::Vector3d v) {
#ifdef NDEBUG
  fmt::print("say/1.0: Hello World Release! v: [{:.3f}, {:.3f}, {:.3f}]\n",
             v.x(), v.y(), v.z());
#else
  fmt::print("say/1.0: Hello World Debug! v: [{:.3f}, {:.3f}, {:.3f}]\n", v.x(),
             v.y(), v.z());
#endif
}
