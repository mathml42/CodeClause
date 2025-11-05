# Image Recognition with OpenCV

## Overview

This project demonstrates basic facial feature detection using OpenCV's Haar cascades. The included `main.py` detects faces, eyes, and smiles in either a static image or a webcam feed and overlays simple graphical markers (ellipses, circles, and lines) to indicate detected features.

## What it does

- Detects faces in an image or webcam stream using OpenCV's pre-trained Haar cascade for frontal faces.
- Within each detected face, detects eyes and smiles using the corresponding Haar cascades.
- Draws a stylized oval around faces, ellipses and small dots for eyes, and a smiling mouth overlay when a smile is detected that looks little fun.

## How it works (brief)

1. The script loads three Haar cascade classifiers shipped with OpenCV: face, eye, and smile.
2. It converts the input frame to grayscale (Haar cascades work on intensity images).
3. `detectMultiScale` is used to find faces in the grayscale image. For each face ROI (region of interest):
	- Eyes are detected and drawn as small ellipses and center dots.
	- Smiles are detected and drawn as a partial ellipse (a mouth) and a line to emphasize the smile.
4. The result is shown in a window. If using the webcam, press `q` to quit; if using an image, the program waits for a keypress and then exits.

## Requirements

- Python 3.8+ (the project was developed using Python 3.12 in a venv included in the repo)
- OpenCV (cv2) — install with pip: `pip install opencv-python`

Optional (recommended):
- A virtual environment to avoid dependency conflicts.

## Installation

1. Create and activate a virtual environment (optional but recommended):

	python -m venv .venv
	source .venv/bin/activate

2. Install dependencies:

	pip install opencv-python

## Usage

Run the main script from the `image-recognition-with-openCV` folder:

1. Using an image:

	python main.py

	When prompted, answer `n` and enter the path to an image file. The program will open a window showing detected features and will close after a keypress.

2. Using the webcam:

	python main.py

	When prompted, answer `y` to use the webcam. The program opens a live window; press `q` to quit.

## License

This project is provided as-is for learning and demonstration purposes. Feel free to adapt and reuse.
