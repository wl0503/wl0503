---
toc: true
comments: true
layout: post
title: data compression
description: 
courses: { compsci: {week: 7} }
type: hacks
---

- Explains data compression as the reduction of the number of bits needed to represent data.
Differentiates between lossy compression, which reduces data but doesn't allow for the full recovery of the original data, and lossless compression, which enables data restoration.
Image Files and Size:

- Discusses image file types such as PNG and JPG.
Mentions considerations like the dimensions (height and width) of images, as well as the number of pixels.
Notes the impact of lossy compression on visual perception.
Displaying Images in Python Jupyter Notebook:

- Introduces Python libraries and concepts used for data visualization in Jupyter notebooks.
Mentions the use of IPython for visualization.
Highlights the importance of pathlib in handling file paths across different operating systems.
Reading and Encoding Images:

- Covers two implementations for reading and encoding images, one using the Python Image Library (PIL) and another using base64.
Utilizes NumPy for creating arrays from image data.
Discusses the importance of input/output (I/O) buffering in handling large image data.
Data Structures and OOP (Object-Oriented Programming):

- emonstrates a transition from imperative programming to object-oriented programming for image data management.
Defines a Python class Image_Data to encapsulate image-related data and operations.
Provides properties for accessing image attributes.
Discusses the organization of data and the use of objects to represent images.