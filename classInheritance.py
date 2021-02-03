class electric:
    def __init__(self, weight, height, width, price, producer):
        self.weight=weight
        self.height=height
        self.width=width
        self.price=price
        self.producer=producer

class TV(electric):
    def __init__(self, weight, height, width, price, producer, inch, brightness, resolution):
        super().__init__(weight, height, width, price, producer)
        self.inch=inch
        self.brightness=brightness
        self.resolution=resolution

    def printDetails(self):
        print('Weight:{}, Height:{}, Width:{}, Price:{}, Producer:{}, Inch:{}, Brightness:{}, Resolution:{}'.format(self.weight, self.height, self.width, self.price, self.producer, self.inch, self.brightness, self.resolution))




#Main
tv1=TV(65, 90, 20, 5765, 'Sony', '65inc', 0.7, '1920x1080')
tv2=TV(40, 60, 14, 3500, 'Sony', '45inc', 0.7, '1920x1080')
tv1.printDetails()
tv2.printDetails()