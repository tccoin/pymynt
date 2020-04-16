# pymynt
A basic Cython wrapper for MYNT depth camera.

## Installation

1. Install [OpenCV](https://opencv.org/releases/)
2. Install [MYNT SDK v1.8](https://mynt-eye-d-sdk.readthedocs.io/en/v1.8.0/sdk/sdk_install.html) (v1.9 has removed some useful API)
3. Install Cython
4. edit `include_dirs` in `setup.py` (remember to use `//` on Windows)
5. run `python setup.py build_ext --inplace`

## Usage

```python
import pymynt

pymynt.init_camera()
depth = pymynt.get_depth_image()
left = pymynt.get_left_image()
right = pymynt.get_right_image()
# for more options, you can edit the wrapper directly and rebuild pymynt
```

## How it works
- Cython is used to call the opencv functions.
- `cv::Mat` is converted to numpy array by[wangzheqie/cpp_python_convert](https://github.com/wangzheqie/cpp_python_convert).
