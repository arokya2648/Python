class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
modelx=vehicle(240, 18)
print('mode1 max speed;',modelx.max_speed)
print('model mileage:', modelx.mileage)