class DeviceNotFoundError(Exception):
    pass

class Device:
    def __init__(self, name):
        self.name = name
        self._status = False
    @property
    def status(self):
        return self._status
    def turn_on(self):
        self._status = True
    def turn_off(self):
        self._status = False

class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self._brightness = 0
    @property
    def brightness(self):
        return self._brightness
    @brightness.setter
    def brightness(self, val):
        if not isinstance(val, int):
            raise ValueError('亮度等级必须为整数')
        elif val < 0:
            raise ValueError('亮度不能为负')
        elif val > 3:
            raise ValueError('亮度最高三级')
        self._brightness = val
        print(f'已设置{self.name}亮度为{self._brightness}')
        if self._brightness == 0:
            super().turn_off()
        else:
            super().turn_on()
    def turn_on(self):
        super().turn_on()
        if self.brightness == 0:
            self.brightness = 2
    def turn_off(self):
        super().turn_off()
        self.brightness = 0

class AC(Device):
    def __init__(self, name):
        super().__init__(name)
        self._temper = None
    @property
    def temper(self):
        return self._temper
    @temper.setter
    def temper(self, val):
        try:
            val = float(val)
        except(ValueError, TypeError):
            raise ValueError('温度必须为数字')
        if not 20 <= val <= 40:
            raise ValueError('温度必须在 20 到 40 之间')
        if (val * 2) % 1 != 0:
            raise ValueError('温度步进为 0.5')
        self._temper = val
        print(f'已设置{self.name}温度为{self._temper}度')
        super().turn_on()
    def turn_on(self):
        super().turn_on()
        if self._temper == None:
            self._temper = 26.0
    def turn_off(self):
        super().turn_off()
        self._temper = None
class HomeSys:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.name] = device
        print(f"设备 [{device.name}] 已添加。")

    def remove_device(self, name):
        if name in self.devices:
            del self.devices[name]
            print(f"设备 [{name}] 已删除。")
        else:
            raise DeviceNotFoundError(f"没有找到设备 [{name}]")

    def get_device(self, name):
        if name in self.devices:
            return self.devices[name]
        else:
            raise DeviceNotFoundError(f"没有找到设备 [{name}]")

home = HomeSys()
light = Light('灯')
ac = AC('空调')
home.add_device(light)
home.add_device(ac)
light.brightness = 3
ac.temper = 29