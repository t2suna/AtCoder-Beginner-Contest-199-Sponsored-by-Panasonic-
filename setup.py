from distutils.core import setup, Extension
from Cython.Build import cythonize
from numpy import get_include # cimport numpy を使うため

ext = Extension("c_c", sources=["c.pyx"], include_dirs=['.', get_include()])
setup(name="c_c", ext_modules=cythonize([ext]))