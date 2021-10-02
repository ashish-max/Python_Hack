import cv2
import numpy as np

from scipy.interpolate import UnivariateSpline

img = cv2.imread("cat.png")

#Warming effect
class WarmingFilter():
    """Cooling filter
        A class that applies a cooling filter to an image.
        The class uses curve filters to manipulate the perceived color
        temparature of an image. The warming filter will shift the image's
        color spectrum towards blue, away from red.
    """

    def __init__(self):
        """Initialize look-up table for curve filter"""
        # create look-up tables for increasing and decreasing a channel
        self.incr_ch_lut = self._create_LUT_8UC1([0, 64, 128, 192, 256],
                                                 [0, 70, 140, 210, 256])
        self.decr_ch_lut = self._create_LUT_8UC1([0, 64, 128, 192, 256],
                                                 [0, 30,  80, 120, 192])

    def render(self, img_rgb):
        """Applies pencil sketch effect to an RGB image
            :param img_rgb: RGB image to be processed
            :returns: Processed RGB image
        """
        # cooling filter: increase blue, decrease red
        c_r, c_g, c_b = cv2.split(img_rgb)
        c_r = cv2.LUT(c_r, self.decr_ch_lut).astype(np.uint8)
        c_b = cv2.LUT(c_b, self.incr_ch_lut).astype(np.uint8)
        img_rgb = cv2.merge((c_r, c_g, c_b))

        # decrease color saturation
        c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV))
        c_s = cv2.LUT(c_s, self.decr_ch_lut).astype(np.uint8)
        return cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)

    def _create_LUT_8UC1(self, x, y):
        """Creates a look-up table using scipy's spline interpolation"""
        spl = UnivariateSpline(x, y)
        return spl(range(256))
print('Warming  Effect Applied.')

x = WarmingFilter()
Warm  = x.render(img)

#comparing original vs resized
cv2.imshow('ORIGINAL',img)
cv2.imshow('Warming effect',Warm)

cv2.waitKey(0)
cv2.destroyAllWindows()


