from conans import ConanFile
import os
from conans.tools import download, unzip, check_sha256
from conans import CMake

class ArbitraryName(ConanFile):
    name = "eggs-cpp-variant"
    version = "2016.2.6"
    branch = "stable"
    license = "Boost"
    generators = "cmake"
    url="http://github.com/TyRoXx/conan-eggs-cpp-variant"
    ZIP_FOLDER_NAME = "variant-11a0fc94e196a101fa38ca74d616792e9b1fc507"

    def source(self):
        zip_name = "variant.zip"
        download("https://github.com/eggs-cpp/variant/archive/11a0fc94e196a101fa38ca74d616792e9b1fc507.zip", zip_name)
        check_sha256(zip_name, "6705a221db0915cd2b18801c17da1ed26e85f1e55885d3c002d6e13c21b8058d")
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*.h*", "include", "%s/include" % self.ZIP_FOLDER_NAME, keep_path=True)
