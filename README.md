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

- The zernike_order_list function calculates Zernike polynomials' factorials, p-indices, and q-indices.
- The robust_fact_quot function removes common elements from lists and calculates product quotients.
- The zernike_bf function generates Zernike basis functions stored in a complex-valued grid.
- The zernike_mom function calculates Zernike moments by summing the product of the image and basis functions.
- The zernike_rec function reconstructs an image by summing the weighted Zernike basis functions based on moments.
- The code utilizes additional helper functions, mathematical calculations, and NumPy operations.
- The functions accept parameters such as image data, maximum order, size, and optional arguments.
- The code includes checks for data validity, such as square image size matching, and prints informative error messages.
- The functions return relevant results, such as Zernike moments or reconstructed images.

## Installation 

1. Download the ZEMO repository.
2. In the main ZEMO directory ```(ZEMO-main\ZEMO\)``` use the package manager [pip](https://pip.pypa.io/en/stable/) to install ```ZEMO``` package:

```bash
pip install .
```
or
```bash
py -m pip install .
```

Now you can use ZEMO package in any local directory on your computer.

## Usage

1. In any Python editor (interpreter) import the ZEMO next to the necessary libraries:
```python
from ZEMO import zemo
```

2. Generates Zernike basis functions for a given `size`, `order`, and optional `withneg` parameter for a **square images** of size **SZ**.
   If withneg is 1, then the basis functions with negative repetition are included.
```python
ZBFSTR = zemo.zernike_bf(SZ,order,withneg) 
```

3. Calculates Zernike moments of an input image (images) using precomputed Zernike basis functions. **I** is the input image.
```python
Z = zemo.zernike_mom(I,ZBFSTR)
```

4. Reconstructs an image from Zernike moments using precomputed Zernike basis functions.
```python
I = zemo.zernike_rec(Z,SZ,ZBFSTR)
```
You can see some examples of the ZM Code Usage.

## Examples

In the following examples, we provide the calculations of Zernike moments for a given image. To validate the calculation, we reconstructed images in different orders of Zernike maximum orders. 
You can use these example images in the Examples directory. Note: Make a Python file in the ```ZEMO-main\ZEMO\Data``` directory and test the examples with the codes provided below.

1. Solar coronal AIA image at 171 Angstrom
   
```python
import numpy as np
import matplotlib.pyplot as plt
from ZEMO import zemo 
import os
from astropy.io import fits
import sunpy.map
from zipfile import ZipFile
import astropy.units as u
from astropy.coordinates import SkyCoord
from matplotlib.patches import ConnectionPatch
from typing_extensions import AsyncIterator

directory_path = r'path\to\your\direcotry\ZEMO-main\ZEMO\Data'
with ZipFile('AIA20200530_145745_0171.rar', 'r') as f:
f.extractall()
AIA = 'AIA20200530_145745_0171.fits'
file_path1 = os.path.join(directory_path,AIA)
aia = sunpy.map.Map(file_path1)
bottom_left = aia.wcs.pixel_to_world(2555 * u.pixel, 2066 * u.pixel)
top_right = aia.wcs.pixel_to_world(2613* u.pixel, 2008 * u.pixel)
fig = plt.figure(figsize=(7, 4.8))
ax1 = fig.add_subplot(121, projection=aia)
aia.plot(axes=ax1,annotate=False)
plt.text(100,3800, '(a)', fontsize=10, fontweight='bold',color='white')
for coord in ax1.coords:
    coord.frame.set_linewidth(1)
    coord.set_ticks_visible(False)
    coord.set_ticklabel_visible(False)
aia.draw_grid(axes=ax1, color='black', alpha=0.25, lw=0.5)
aia.draw_quadrangle(bottom_left, top_right=top_right, edgecolor='black', lw=1)
aia_sub = aia.submap(bottom_left, top_right=top_right)

left, width = 0.3, 0.2
bottom, height = 0.55, .2
rect_box = [left, bottom, width, height]
ax2 = plt.axes(rect_box,projection=aia_sub)
aia_sub.plot(axes=ax2, annotate=False)
for coord in ax2.coords:
    coord.frame.set_linewidth(2)
    coord.set_ticks_visible(False)
    coord.set_ticklabel_visible(False)
xpix, ypix = aia.wcs.world_to_pixel(SkyCoord(top_right.Tx, top_right.Ty, frame=aia.coordinate_frame))
con1 = ConnectionPatch((1, 0), (xpix, ypix), 'axes fraction', 'data', axesA=ax2, axesB=ax1, arrowstyle='-', color='black', lw=1)
xpix, ypix = aia.wcs.world_to_pixel(bottom_left)
con2 = ConnectionPatch((0, 0), (xpix, ypix), 'axes fraction', 'data', axesA=ax2, axesB=ax1, arrowstyle='-', color='black', lw=1)
ax2.add_artist(con1)
ax2.add_artist(con2)
ax2.grid(alpha=0)
ax1.grid(alpha=0)

SZ=np.shape(aia_sub.data)
ZBFSTR=zemo.zernike_bf(SZ[0],25,1)
Z1=zemo.zernike_mom(aia_sub.data,ZBFSTR)
left, width = 0.6, 0.28
bottom, height = 0.55, .25
rect_box = [left, bottom, width, height]
box = plt.axes(rect_box)
plt.scatter(Z1.real,Z1.imag,facecolor='black',color='tomato')
plt.text(220000,21000, '(b)', fontsize=10,color='black')
plt.ylabel('Imaginary',fontsize=10)
plt.xlabel('Real',fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.grid(alpha=0)

left, width = 0.6, 0.28
bottom, height = 0.18, .25
rect_box = [left, bottom, width, height]
box = plt.axes(rect_box)
box.plot(np.abs(Z1)/np.max(np.abs(Z1)),lw=.9)
plt.text(320,0.9, '(c)', fontsize=10,color='black')
plt.xlabel('(p,q)',fontsize=10)
plt.ylabel('Normalized  $|Z_{pq}|$',fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.grid(alpha=0)
```
<p align="center">
<img src="https://github.com/hmddev1/ZM/assets/53661111/17d2dcb3-6816-45c1-b1bd-53ddf39b857e" alt="AIA" width="500">
</p>
<!-- ![AIA](https://github.com/hmddev1/ZM/assets/53661111/17d2dcb3-6816-45c1-b1bd-53ddf39b857e) -->


2. Face image: (Face: Hossein Safari)

```python
import numpy as np
import matplotlib.pyplot as plt
from ZEMO import zemo 

img = plt.imread('HS.png')

fig, axes = plt.subplots(nrows=4, ncols=1,figsize=(6,6))
plt.subplot(1,4,1)
plt.imshow(img, interpolation='nearest',cmap='bone')
plt.title('Original Image', fontsize=9)
plt.axis('off')
SZ=np.shape(img)
Order=[10,45,46]

for i in range(3):
   ZBFSTR=zemo.zernike_bf(SZ[0],Order[i],1)
   Z=zemo.zernike_mom(np.double(img),ZBFSTR)
   I=zemo.zernike_rec(Z,SZ[0],ZBFSTR)
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


3. The original and reconstructed image of a spiral galaxy (top row), elliptical galaxy (middle row), and irregular galaxy (bottom row) recorded by the SDSS survey.

```python
import os
import numpy as np
import matplotlib.pyplot as plt
from ZEMO import zemo
from astropy.io import fits

directory_path = r'path\to\your\direcotry\ZEMO-main\ZEMO\Data'          # You need to read an example FITS file from the directory: ZM-main\ZM\Data\
filename = 'PGC0023498.fits'          # You can also test the "PGC0054488.fits" and "PGC0057771.fits" files

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
   ZBFSTR=zemo.zernike_bf(SZ[0],Order[i],1)
   Z=zemo.zernike_mom(np.double(data),ZBFSTR)
   I=zemo.zernike_rec(Z,SZ[0],ZBFSTR)
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

[Hamed Ghaderi](https://github.com/hmddev1), [Nasibe Alipour](https://scholar.google.com/citations?user=PfzZOI0AAAAJ&hl=en), [Hossein Safari](https://scholar.google.com/citations?user=nCc1FV8AAAAJ&hl=en), [Pardis Garavand](https://www.linkedin.com/in/pardis-garavand-25b30527b/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
