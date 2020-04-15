cimport numpy as np
import numpy as np

# For cv::Mat usage
cdef extern from "opencv2/core/core.hpp":
  cdef int  CV_WINDOW_AUTOSIZE
  cdef int CV_8UC3
  cdef int CV_8UC1
  cdef int CV_16UC1
  cdef int CV_32FC1
  cdef int CV_8U
  cdef int CV_32F

cdef extern from "opencv2/core/core.hpp" namespace "cv":
  cdef cppclass Mat:
    Mat() except +
    void create(int, int, int)
    void* data
    int rows
    int cols
    int channels()
    int depth()
    size_t elemSize()

# For Buffer usage
cdef extern from "Python.h":
  ctypedef struct PyObject
  object PyMemoryView_FromBuffer(Py_buffer *view)
  int PyBuffer_FillInfo(Py_buffer *view, PyObject *obj, void *buf, Py_ssize_t len, int readonly, int infoflags)
  enum:
      PyBUF_FULL_RO

cdef extern from "mynteyed/device/types.h" namespace "mynteyed":
  cdef cppclass DepthMode:
    pass

cdef extern from "mynteyed/device/types.h" namespace "mynteyed::DepthMode":
  cdef DepthMode DEPTH_RAW
  cdef DepthMode DEPTH_GRAY
  cdef DepthMode DEPTH_COLORFUL

# cdef extern from "mynteyed/device/types.h" namespace "mynteyed::DepthMode":
#     cdef enum DepthMode "mynteyed::DepthMode":
#       DEPTH_RAW      = 0
#       DEPTH_GRAY     = 1
#       DEPTH_COLORFUL = 2

cdef extern from "wrapper.cpp":
  int init(int depth_mode)
  Mat getDepthImage()
  Mat getLeftImage()
  Mat getRightImage()
  