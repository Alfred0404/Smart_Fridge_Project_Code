# Smart Fridge (**WIP**)

This project involves developing a smart fridge that tracks the items stored inside and suggests recipes based on the available ingredients.

## Getting Started

Clone the project on your machine

```
git clone https://github.com/Alfred0404/Smart_Fridge_Project_Code.git
```

### Prerequisites

You need [Python &gt;3.11](https://www.python.org/downloads/) and some dependencies:

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Ollama](https://github.com/ollama/ollama-python)
- [OpenCV](https://vovkos.github.io/doxyrest-showcase/opencv/sphinx_rtd_theme/index.html#)
- [Ultralytics](https://docs.ultralytics.com/quickstart/#install-ultralytics)
- [EasyOCR](https://pypi.org/project/easyocr/)

```
pip install opencv-python ollama Flask ultralytics easyocr
```

## Dataset

To train the Yolov11n model, a [dataset containing fridge](https://universe.roboflow.com/fridge-6oahv/fridge-vstlk) items has been used.

## Training



## Authors

- **Alfred de Vulpian** - [Alfred0404](https://github.com/Alfred0404)
- **Clément d'Alberto** - [Clement-dl](https://github.com/https://github.com/Clement-dl)
- **Alara Tanguy** - [AlTang01](https://github.com/AlTang01)

See the list of [contributors](https://github.com/Alfred0404/Smart_Fridge_Project_Code/contributors) who participated in this project.


# References

```
@software{yolo11_ultralytics,
  author = {Glenn Jocher and Jing Qiu},
  title = {Ultralytics YOLO11},
  version = {11.0.0},
  year = {2024},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}

@article{OpenImages,
  author = {Alina Kuznetsova and Hassan Rom and Neil Alldrin and Jasper Uijlings and Ivan Krasin and Jordi Pont-Tuset and Shahab Kamali and Stefan Popov and Matteo Malloci and Alexander Kolesnikov and Tom Duerig and Vittorio Ferrari},
  title = {The Open Images Dataset V4: Unified image classification, object detection, and visual relationship detection at scale},
  year = {2020},
  journal = {IJCV}
}
```