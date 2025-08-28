import time

class Car:
    def __init__(self, marka, max_speed):
        self.marka = marka
        self.speed = 0
        self.max_speed = max_speed

    def accelerate(self, step=20):

        if self.speed < self.max_speed:
            self.speed += step
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        print(f"{self.marka} hozir {self.speed} km/h tezlikda ketmoqda.")


bmw = Car("BMW", 360)



while bmw.speed < bmw.max_speed:
    bmw.accelerate(10)
    time.sleep(1)
