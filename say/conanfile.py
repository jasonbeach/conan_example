import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.files import  load

class SayConan(ConanFile):
    name = "say"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "version.txt", "*-config.cmake.in"

    def set_version(self):
        self.version = load(self, "version.txt").strip()
        
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires('fmt/10.0.0')
        self.requires('eigen/3.4.0')

    def layout(self):
        cmake_layout(self)
        ## cpp.source is specifically designed for editable packages:
        # because our headers are all in src instead of just 
        self.cpp.source.includedirs = ["src"] # maps to ./src

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        cd = CMakeDeps(self)
        cd.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_target_name", "ns::say")
        self.cpp_info.libs = ["say"]
