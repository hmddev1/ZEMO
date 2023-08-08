import setuptools


setuptools.setup(
    name='ZM',
    version='1.0.0',
    # scripts=['zernikim'] ,
    description='Zernike Moments - Astronomical and none-astronomical images. This code calculates Zernike moments for astronomical images. Zernike moments are unique due to orthogonality and a complete set of Zernike polynomials. Zernike moments are used in image analysis to characterize the shape and structure of objects. The following articles and their references give a detailed description of the Zernike polynomials and Zernike moments.',
    author='Hamed Ghaderi',
    author_email='h.ghaderi@znu.ac.ir',
    packages=['ZM'],
    install_requires=[
        'astropy',
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
 ],
    url='https://github.com/hmddev1/ZM',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)