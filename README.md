# Face-Detection-
This repository contains code that can be used to detect human faces real-time including a human's face,eye and smile

Face detection involves identifying a person’s face in an image or video. This is done by analyzing the visual
input to determine whether a person’s facial features are present.

Since human faces are so diverse, face detection models typically need to be trained on large amounts of input 
data for them to be accurate. The training dataset must contain a sufficient representation of people who come 
from different backgrounds, genders, and cultures.

These algorithms also need to be fed many training samples comprising different lighting, angles, and orientations
to make correct predictions in real-world scenarios.

These nuances make face detection a non-trivial, time-consuming task that requires hours of model training and millions of data samples.

Thankfully, the OpenCV package comes with pre-trained models for face detection, which means that we don’t have to 
train an algorithm from scratch. More specifically, the library employs a machine learning approach called Haar cascade 
to identify objects in visual data.

**Intro to Haar Cascade Classifiers**
This method was first introduced in the paper Rapid Object Detection Using a Boosted Cascade of Simple Features, 
written by Paul Viola and Michael Jones.

The idea behind this technique involves using a cascade of classifiers to detect different features in an image.
These classifiers are then combined into one strong classifier that can accurately distinguish between samples that contain a human face from those that don’t.

The Haar Cascade classifier that is built into OpenCV has already been trained on a large dataset of human faces, 
so no further training is required. We just need to load the classifier from the library and use it to perform face detection on an input image.
