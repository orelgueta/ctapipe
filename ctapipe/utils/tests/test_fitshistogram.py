# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np
from ..fitshistogram import Histogram


def test_histogram_str():
    hist = Histogram(nbins=[5, 10], ranges=[[-2.5, 2.5], [-1, 1]], name="testhisto")
    expected = "Histogram(name='testhisto', axes=['axis0', 'axis1'], nbins=[ 5 10], ranges=[[-2.5  2.5]\n [-1.   1. ]])"
    assert str(hist) == expected


def test_histogram_fill_and_read():

    hist = Histogram(nbins=[5, 10], ranges=[[-2.5, 2.5], [-1, 1]])

    pa = (0.1, 0.1)
    pb = (-0.55, 0.55)

    a = np.ones((100, 2)) * pa  # point at 0.1,0.1
    b = np.ones((10, 2)) * pb  # 10 points at -0.5,0.5

    hist.fill(a)
    hist.fill(b)

    va = hist.getValue(pa)[0]
    vb = hist.getValue(pb)[0]

    assert va == 100
    assert vb == 10


def test_histogram_range_fill_and_read():
    """
    Check that the correct bin is read and written for multiple
    binnings and fill positions
    """

    N = 100

    for nxbins in np.arange(1, 50, 1):
        for xx in np.arange(-2.0, 2.0, 0.1):
            pp = (xx + 0.01829384, 0.1)
            coords = np.ones((N, 2)) * pp
            hist = Histogram(nbins=[nxbins, 10],
                             ranges=[[-2.5, 2.5], [-1, 1]])
            hist.fill(coords)
            val = hist.getValue(pp)[0]
            assert val == N
            del hist

# def testOutliers(self):
#     """
#     Check that out-of-range values work as expected
#     """
#     H = fitshistogram.Histogram( nbins=[5,10], range=[[-2.5,2.5],[-1,1]] )
#     H.fill( np.array( [[1,1],]) )
#     val1= H.getValue( (100,100), outlierValue = -10000)[0]
#     val2= H.getValue( (-100,0), outlierValue = None)[0]
#     self.assertEqual(val1,-10000)
#     self.assertEqual(val2,0)

def test_histogram_write_fits():
    """
    Write to fits,read back, and check
    """
    # TODO: implement
    pass