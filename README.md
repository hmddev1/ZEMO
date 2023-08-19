# Zernike moments: Digital images

The Zernike moment's package program is developed for square digital images mimicking some part of Matlab code provided by Christian Wolf. Zernike moments are unique due to orthogonality and a complete set of Zernike polynomials. Zernike moments are used in image analysis to characterize the shape and structure of objects. The following articles and their references give a detailed description of the Zernike polynomials and Zernike moments.

[Raboonik, A., Safari, H., Alipour, N., & Wheatland, M. S. 2017, ApJ, 834, 11](https://iopscience.iop.org/article/10.3847/1538-4357/834/1/11/meta)

[Alipour, N., Mohammadi, F., Safari, H. 2019, ApJS, 243, 20](https://iopscience.iop.org/article/10.3847/1538-4365/ab289b/meta)

## Description 

The code includes the following functions:

**zernike_order_list**: Generates a list of Zernike polynomial orders.

**robust_fact_quot**: Calculates the robust factor quotient between two lists of values.

**zernike_bf**: Generates Zernike basis functions for a given size and order.

**zernike_mom**: Calculates the Zernike moments of an input image using precomputed Zernike basis functions.

**zernike_rec**: Reconstructs an image from Zernike moments(Inverse trasformation).

### Notes

- The zernike_order_list function calculates factorials, p-indices, and q-indices for Zernike polynomials.
- The robust_fact_quot function removes common elements from lists and calculates product quotients.
- The zernike_bf function generates Zernike basis functions stored in a complex-valued grid.
- The zernike_mom function calculates Zernike moments by summing the product of the image and basis functions.
- The zernike_rec function reconstructs an image by summing the weighted Zernike basis functions based on moments.
- The code utilizes additional helper functions, mathematical calculations, and NumPy operations.
- The functions accept parameters such as image data, maximum order, size, and optional arguments.
- The code includes checks for data validity, such as square image size matching, and prints informative error messages.
- The functions return relevant results, such as Zernike moments or reconstructed images.

## Installation 

1. Download the ZM repository.
2. In the main ZM directory ```(ZM-main\ZM\)``` use the package manager [pip](https://pip.pypa.io/en/stable/) to install ZM package:

```bash
!pip install .
```
or
```bash
py -m pip install .
```

Now you can use ZM package in any local directory on your computer.

## Usage

1. In any Python editor (interpreter) import the ZM next to the necessary libraries:
```python
from ZM import zernikim as zm
```

2. Generates Zernike basis functions for a given `size`, `order`, and optional `withneg` parameter for a **square images** of size **SZ**.
   If withneg is 1, then the basis functions with negative repetition are included.
```python
ZBFSTR = zm.zernike_bf(SZ,order,withneg) 
```

3. Calculates Zernike moments of an input image (images) using precomputed Zernike basis functions. **I** is the input image.
```python
Z = zm.zernike_mom(I,ZBFSTR)
```

4. Reconstructs an image from Zernike moments using precomputed Zernike basis functions.
```python
I = zm.zernike_rec(Z,SZ,ZBFSTR)
```
You can see some examples of the ZM Code Usage.

## Examples

In the following examples, we provide the calculations of Zernike moments for a given image. To validate the calculation, we reconstructed images in different orders of Zernike maximum orders. 
You can use these example images in the Examples directory. Note: Make a Python file in the ```ZM-main\ZM\Examples``` directory and test the examples with the codes provided below.

1. Face image: (Face: Hossein Safari)

```python
import numpy as np
import matplotlib.pyplot as plt
from ZM import zernikeim as zm

img = plt.imread('HS.png')

fig, axes = plt.subplots(nrows=4, ncols=1,figsize=(6,6))
plt.subplot(1,4,1)
plt.imshow(img, interpolation='nearest',cmap='bone')
plt.title('Original Image', fontsize=9)
plt.axis('off')
SZ=np.shape(img)
Order=[10,45,46]

for i in range(3):
   ZBFSTR=zm.zernike_bf(SZ[0],Order[i],1)
   Z=zm.zernike_mom(np.double(img),ZBFSTR)
   I=zm.zernike_rec(Z,SZ[0],ZBFSTR)
   plt.subplot(1,4,i+2)
   plt.imshow(I,interpolation='nearest',cmap='bone')
   plt.title('$P_{max}$='+ str(Order[i]), fontsize=9)
   plt.axis('off')
plt.show()
```
<p align="center">
<img src="https://github.com/hmddev1/ZM/assets/53661111/51055b70-0b3e-453e-83bf-c5f0275fb1d1" alt="HS" width="500">
</p>
<!-- ![HS](https://github.com/hmddev1/ZM/assets/53661111/51055b70-0b3e-453e-83bf-c5f0275fb1d1) -->


2. The original and reconstructed image of a spiral galaxy (top row), elliptical galaxy (middle row), and irregular galaxy (bottom row) recorded by the SDSS survey.

```python
import os
import numpy as np
import matplotlib.pyplot as plt
from ZM import zernikim as zm
import astropy
from astropy.io import fits

directory_path = r'path\to\your\direcotry\ZM-main\ZM\Examples'          # You need to read an example FITS file from the directory: ZM-main\ZM\Examples\
filename = 'S.fits'          # You can also test the "E.fits" and "I.fits" files

file_path = os.path.join(directory_path, filename)
hdul = fits.open(file_path)
data = hdul[0].data
hdul.close()

fig, axes = plt.subplots(nrows=4, ncols=1,figsize=(6,6))
plt.subplot(1,4,1)
plt.imshow(data, interpolation='nearest',cmap='bone')
plt.title('Original Image', fontsize=9)
plt.axis('off')
SZ=np.shape(data)
Order=[10,45,47]

for i in range(3):
   ZBFSTR=zm.zernike_bf(SZ[0],Order[i],1)
   Z=zm.zernike_mom(np.double(data),ZBFSTR)
   I=zm.zernike_rec(Z,SZ[0],ZBFSTR)
   plt.subplot(1,4,i+2)
   plt.imshow(I,interpolation='nearest',cmap='bone')
   plt.title('$P_{max}$='+ str(Order[i]), fontsize=9)
   plt.axis('off')
plt.show()
```

<p align="center">
<img src="https://github.com/hmddev1/ZM/assets/53661111/5f220f89-cf97-48c3-a3b4-52911b84b78e" alt="Spiral_rec" width="500">
<!-- ![Spiral_rec](https://github.com/hmddev1/ZM/assets/53661111/5f220f89-cf97-48c3-a3b4-52911b84b78e) -->

<img src="https://github.com/hmddev1/ZM/assets/53661111/efeb672c-2f96-44f5-923e-ef40b0b4e594" alt="Elliptical_rec" width="500">
<!-- ![Elliptical_rec](https://github.com/hmddev1/ZM/assets/53661111/efeb672c-2f96-44f5-923e-ef40b0b4e594) -->

<img src="https://github.com/hmddev1/ZM/assets/53661111/58cd6840-3c85-4b5a-bd34-3acfb645e391" alt="Irregular_rec" width="500">
<!-- ![Irregular_rec](https://github.com/hmddev1/ZM/assets/53661111/58cd6840-3c85-4b5a-bd34-3acfb645e391) -->
</p>

## Authors

[Hamed Ghaderi](https://github.com/hmddev1), [Nasibe Alipour](https://scholar.google.com/citations?user=PfzZOI0AAAAJ&hl=en), [Pardis Garavand](https://www.linkedin.com/in/pardis-garavand-25b30527b/), [Hossein Safari](https://scholar.google.com/citations?user=nCc1FV8AAAAJ&hl=en)

## License
[MIT](https://choosealicense.com/licenses/mit/)
