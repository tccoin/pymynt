#ifndef MYNTEYED_PY_WRAPPER_H
#define MYNTEYED_PY_WRAPPER_H

#include <mynteyed/camera.h>
#include <opencv2/highgui/highgui.hpp>

int init(int depth_mode);
cv::Mat getDepthImage();
cv::Mat getRightImage();
cv::Mat getLeftImage();

#endif