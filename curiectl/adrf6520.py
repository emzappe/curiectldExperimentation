import numpy as np

from periphery import SPI

class ADRF6520:
    def __init__(self, spi):
        self._spi = spi
        self._cutoff = 'bypass'
        self._pdn = False
        
    @property
    def cutoff(self):
        return self._cutoff

    @cutoff.setter
    def cutoff(self, v):
        if v not in [ '36MHz', '72MHz', '144MHz', '288MHz', '432MHz', '576MHz', '720MHz', 'bypass' ]:
            print(f"Invalid cutoff. Options are 36MHz, 72MHz, 144MHz, 288MHz, 432MHz, 576MHz, 720MHz, and bypass.")
        self._cutoff = v
        self.update()
        
    @property
    def pdn(self):
        return self._pdn

    @pdn.setter
    def pdn(self, v):
        self._pdn = v
        self.update()

    def program(self):
        if self._cutoff == '36MHz':
            bits = 0x0
        elif self._cutoff == '72MHz':
            bits = 0x1
        elif self._cutoff == '144MHz':
            bits = 0x2
        elif self._cutoff == '288MHz':
            bits = 0x3
        elif self._cutoff == '432MHz':
            bits = 0x4
        elif self._cutoff == '576MHz':
            bits = 0x5
        elif self._cutoff == '720MHz':
            bits = 0x6
        elif self._cutoff == 'bypass':
            bits = 0x7

        if not self._pdn:
            bits |= 0x80
            
        self._spi.transfer([ 0x00, 0x10, bits ])

    gain_table = np.array([
        [ 0.   , 0.   ],
        [ 0.5  , 0.16 ],
        [ 1.   , 0.188],
        [ 1.5  , 0.208],
        [ 2.   , 0.225],
        [ 2.5  , 0.24 ],
        [ 3.   , 0.253],
        [ 3.5  , 0.265],
        [ 4.   , 0.277],
        [ 4.5  , 0.287],
        [ 5.   , 0.297],
        [ 5.5  , 0.307],
        [ 6.   , 0.316],
        [ 6.5  , 0.325],
        [ 7.   , 0.334],
        [ 7.5  , 0.343],
        [ 8.   , 0.351],
        [ 8.5  , 0.359],
        [ 9.   , 0.367],
        [ 9.5  , 0.375],
        [10.   , 0.383],
        [10.5  , 0.391],
        [11.   , 0.398],
        [11.5  , 0.406],
        [12.   , 0.413],
        [12.5  , 0.42 ],
        [13.   , 0.428],
        [13.5  , 0.435],
        [14.   , 0.442],
        [14.5  , 0.449],
        [15.   , 0.456],
        [15.5  , 0.463],
        [16.   , 0.47 ],
        [16.5  , 0.477],
        [17.   , 0.484],
        [17.5  , 0.491],
        [18.   , 0.498],
        [18.5  , 0.505],
        [19.   , 0.512],
        [19.5  , 0.519],
        [20.   , 0.526],
        [20.5  , 0.533],
        [21.   , 0.541],
        [21.5  , 0.548],
        [22.   , 0.555],
        [22.5  , 0.562],
        [23.   , 0.569],
        [23.5  , 0.576],
        [24.   , 0.583],
        [24.5  , 0.59 ],
        [25.   , 0.597],
        [25.5  , 0.604],
        [26.   , 0.612],
        [26.5  , 0.619],
        [27.   , 0.626],
        [27.5  , 0.633],
        [28.   , 0.641],
        [28.5  , 0.648],
        [29.   , 0.655],
        [29.5  , 0.662],
        [30.   , 0.67 ],
        [30.5  , 0.677],
        [31.   , 0.684],
        [31.5  , 0.692],
        [32.   , 0.699],
        [32.5  , 0.707],
        [33.   , 0.714],
        [33.5  , 0.721],
        [34.   , 0.729],
        [34.5  , 0.736],
        [35.   , 0.744],
        [35.5  , 0.751],
        [36.   , 0.758],
        [36.5  , 0.766],
        [37.   , 0.773],
        [37.5  , 0.781],
        [38.   , 0.788],
        [38.5  , 0.796],
        [39.   , 0.803],
        [39.5  , 0.811],
        [40.   , 0.818],
        [40.5  , 0.826],
        [41.   , 0.833],
        [41.5  , 0.841],
        [42.   , 0.848],
        [42.5  , 0.856],
        [43.   , 0.863],
        [43.5  , 0.871],
        [44.   , 0.878],
        [44.5  , 0.886],
        [45.   , 0.894],
        [45.5  , 0.901],
        [46.   , 0.909],
        [46.5  , 0.917],
        [47.   , 0.925],
        [47.5  , 0.933],
        [48.   , 0.941],
        [48.5  , 0.949],
        [49.   , 0.957],
        [49.5  , 0.965],
        [50.   , 0.974],
        [50.5  , 0.982],
        [51.   , 0.991],
        [51.5  , 1.   ],
        [52.   , 1.009],
        [52.5  , 1.018],
        [53.   , 1.027],
        [53.5  , 1.037],
        [54.   , 1.047],
        [54.5  , 1.057],
        [55.   , 1.068],
        [55.5  , 1.079],
        [56.   , 1.091],
        [56.5  , 1.104],
        [57.   , 1.117],
        [57.5  , 1.132],
        [58.   , 1.148],
        [58.5  , 1.167],
        [59.   , 1.19 ],
        [59.5  , 1.22 ],
        [60.   , 1.276]
    ])

    #gain_voltage = np.interp(gain_table[:,0], gain_table[:,1])
    

adrf6520 = {
    'rx0': ADRF6520(SPI("/dev/spidev1.2", 0, 1000000)),
    'rx1': ADRF6520(SPI("/dev/spidev1.3", 0, 1000000)),
    'tx0': ADRF6520(SPI("/dev/spidev1.4", 0, 1000000)),
    'tx1': ADRF6520(SPI("/dev/spidev1.5", 0, 1000000))
}
