from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import subprocess

proc_libs = subprocess.check_output("pkg-config --libs opencv".split())
proc_incs = subprocess.check_output("pkg-config --cflags opencv".split())
libs = [lib for lib in str(proc_libs).split()]

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(Extension("pymynt",
                                    sources=["pymynt.pyx"],
                                    language="c++",
                                    libraries=["mynteye_depth"],
                                    include_dirs=[
                                        numpy.get_include(), "/usr/include/"],
                                    extra_link_args=['-lopencv_dnn', '-lopencv_ml', '-lopencv_objdetect', '-lopencv_shape', '-lopencv_stitching', '-lopencv_superres', '-lopencv_videostab', '-lopencv_calib3d',
                                                     '-lopencv_features2d', '-lopencv_highgui', '-lopencv_videoio', '-lopencv_imgcodecs', '-lopencv_video', '-lopencv_photo', '-lopencv_imgproc', '-lopencv_flann', '-lopencv_core']
                                    )
                          )
)
