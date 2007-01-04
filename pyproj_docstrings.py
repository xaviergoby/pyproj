# this is just a container for the docstrings (to make
# pydoc generated docs, since Pyrex hides docstrings for special
# methods like __call__).
"""
Pyrex wrapper to provide python interfaces to 
PROJ.4 (http://proj.maptools.org) functions.

Performs cartographic transformations (converts from longitude,latitude
to native map projection x,y coordinates and vice versa, or from
one map projection coordinate system directly to another).

Example usage:

>>> from pyproj import Proj
>>> p = Proj(proj='utm',zone=10,ellps='WGS84')
>>> x,y = p(-120.108, 34.36116666)
>>> print x,y
>>> print p(x,y,inverse=True)
765975.641091 3805993.13406
(-120.10799999995851, 34.361166659972767)

Input coordinates can be given as python arrays, lists/tuples, scalars
or numpy/Numeric/numarray arrays. Optimized for objects that support
the Python buffer protocol (regular python and numpy array objects).

Download: http://python.org/pypi/pyproj

Requirements: PROJ.4 library (http://proj.maptools.org).

Install:  Set the PROJ_DIR environment variable to point to the location 
          of your proj.4 installation, then run 'python setup.py install'.
          If you're using Windows with mingw, see README.mingw.

Example scripts are in 'test' subdirectory of source distribution.

Contact:  Jeffrey Whitaker <jeffrey.s.whitaker@noaa.gov

copyright (c) 2006 by Jeffrey Whitaker.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both the copyright notice and this permission notice appear in
supporting documentation.
THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
""" 

__version__ = "1.8.1"

class Proj(object):
    """
 performs cartographic transformations (converts from longitude,latitude
 to native map projection x,y coordinates and vice versa) using proj 
 (http://proj.maptools.org/)

 A Proj class instance is initialized with 
 proj map projection control parameter key/value pairs.
 The key/value pairs can either be passed in a dictionary,
 or as keyword arguments.
 See http://www.remotesensing.org/geotiff/proj_list for
 examples of key/value pairs defining different map projections.

 Calling a Proj class instance with the arguments lon, lat will
 convert lon/lat (in degrees) to x/y native map projection 
 coordinates (in meters).  If optional keyword 'inverse' is
 True (default is False), the inverse transformation from x/y
 to lon/lat is performed. If optional keyword 'radians' is True
 (default is False) lon/lat are interpreted as radians instead
 of degrees. If optional keyword 'errcheck' is True (default is 
 False) an exception is raised if the transformation is invalid.
 If errcheck=False and the transformation is invalid, no execption
 is raised and the platform dependent value HUGE_VAL is returned.
 Works with numpy and regular python array objects, python sequences
 and scalars, but is fastest for array objects. lon and
 lat must be of same type (array, list/tuple or scalar) and have the
 same length (if array, list or tuple).
    """

    def __new__(self, projparams=None, **kwargs):
        """
 initialize a Proj class instance.

 Proj4 projection control parameters must either be
 given in a dictionary 'projparams' or as keyword arguments.
 See the proj documentation (http://proj.maptools.org) for more
 information about specifying projection parameters.
        """
        pass

    def _fwd(self, lons, lats, radians=False, errcheck=False):
        """
 forward transformation - lons,lats to x,y.
 if radians=True, lons/lats are radians instead of degrees.
 if errcheck=True, an exception is raised if the forward transformation is invalid.
 if errcheck=False and the forward transformation is invalid, no exception is
 raised and the platform dependent value HUGE_VAL is returned.
        """
        pass

    def _inv(self, x, y, radians=False, errcheck=False):
        """
 inverse transformation - x,y to lons,lats.
 if radians=True, lons/lats are radians instead of degrees.
 if errcheck=True, an exception is raised if the inverse transformation is invalid.
 if errcheck=False and the inverse transformation is invalid, no exception is
 raised and the platform dependent value HUGE_VAL is returned.
        """
        pass

    def __call__(self,lon,lat,inverse=False,radians=False,errcheck=False):
        """
 Calling a Proj class instance with the arguments lon, lat will
 convert lon/lat (in degrees) to x/y native map projection 
 coordinates (in meters).  If optional keyword 'inverse' is
 True (default is False), the inverse transformation from x/y
 to lon/lat is performed.  If optional keyword 'radians' is
 True (default is False) the units of lon/lat are radians instead
 of degrees. If optional keyword 'errcheck' is True (default is 
 False) an exception is raised if the transformation is invalid.
 If errcheck=False and the transformation is invalid, no execption
 is raised and the platform dependent value HUGE_VAL is returned.

 Inputs should be doubles (they will be cast to doubles
 if they are not, causing a slight performance hit).

 Works with numpy and regular python array objects, python sequences
 and scalars, but is fastest for array objects. lon and
 lat must be of same type (array, list/tuple or scalar) and have the
 same length (if array, list or tuple).
        """
        pass

    def is_latlong(self):
        """returns True if projection in geographic (lon/lat) coordinates"""
        pass

    def is_geocent(self):
        """returns True if projection in geocentric (x/y) coordinates"""
        pass

def transform(p1, p2, x, y, z=None, radians=False):
    """
 x2, y2, z2 = transform(p1, p2, x1, y1, z1, radians=False)

 Transform points between two coordinate systems defined
 by the Proj instances p1 and p2.

 The points x1,y1,z1 in the coordinate system defined by p1
 are transformed to x2,y2,z2 in the coordinate system defined by p2.

 z1 is optional, if it is not set it is assumed to be zero (and 
 only x2 and y2 are returned).

 In addition to converting between cartographic and geographic
 projection coordinates, this function can take care of datum shifts
 (which cannot be done using the __call__ method of the Proj instances).
 It also allows for one of the coordinate systems to be geographic 
 (proj = 'latlong'). 

 If optional keyword 'radians' is True (default is False) and
 p1 is defined in geographic coordinate (pj.is_latlong() is True),
 x1,y1 is interpreted as radians instead of the default degrees.
 Similarly, if p2 is defined in geographic coordinates 
 and radians=True, x2, y2 are returned in radians instead of degrees.
 if p1.is_latlong() and p2.is_latlong() both are False, the
 radians keyword has no effect.

 x,y and z can be numpy or regular python arrays,
 python lists/tuples or scalars. Arrays are fastest. x,y and z must be
 all of the same type (array, list/tuple or scalar), and have the 
 same length (if arrays, lists or tuples).
 For projections in geocentric coordinates, values of
 x and y are given in meters.  z is always meters.
    """
    pass
