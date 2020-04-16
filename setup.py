from distutils.core import setup
import setuptools
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy

ext_modules = cythonize(
    Extension("pymynt",
        sources=["pymynt.pyx"],
        language="c++",
        libraries=["mynteye_depth"],
        include_dirs=[
            numpy.get_include(),
            "/usr/include/"
        ],
        # extra_link_args=['-lopencv_dnn', '-lopencv_ml', '-lopencv_objdetect', '-lopencv_shape', '-lopencv_stitching', '-lopencv_superres', '-lopencv_videostab', '-lopencv_calib3d',
        #                     '-lopencv_features2d', '-lopencv_highgui', '-lopencv_videoio', '-lopencv_imgcodecs', '-lopencv_video', '-lopencv_photo', '-lopencv_imgproc', '-lopencv_flann', '-lopencv_core']
        extra_link_args=['-lopencv_imgproc']
        )
)

setup(
    name='pymynt',
    version='0.1',
    description='A Cython wrapper for MYNT depth camera.',
    author='Tccoin',
    author_email='coin12@qq.com',
    install_requires=['cython'],
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
