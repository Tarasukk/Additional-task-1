import math


class Ball:
    def __init__(self, x: float, y: float, radious: int, direction: int, speed: int):
        self.x = x
        self.y = y
        self.radious = radious
        self.direction = direction
        self.speed = speed
        self.x_delta = speed * math.cos(math.degrees(direction))
        self.y_delta = -speed * math.cos(math.degrees(direction))

    # def setX(self):
    #     self.x = x

    def getX(self):
        return int(self.x)

    # def setY(self):
    #     self.x = x

    def getY(self):
        return int(self.y)

    def getRadious(self):
        return self.radious

    def getSpeed(self):
        return int(math.sqrt(self.x_delta * self.x_delta + self.y_delta * self.y_delta))

    def getDirection(self):
        return int(math.atan2(-self.y_delta, self.x_delta))

    # def setXY(self):
    #     self.x = x
    #     self.y = y

    def move(self):
        self.x += self.x_delta
        self.y += self.y_delta

    def reflectH(self):
        self.x_delta = -1 * self.x_delta

    def reflectY(self):
        self.y_delta = int(-1 * self.y_delta)

    def toString(self):
        return (
            "Ball at (",
            int(self.x),
            ", ",
            int(self.y),
            ") of velocity (",
            self.getSpeed(),
            ",",
            self.getDirection(),
            ")",
        )


class Container:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = self.x + width - 1
        self.y2 = self.y + height - 1

    def collides_with(self, ball: Ball) -> bool:
        if self.width > ball.x > self.x and self.height > ball.y > self.y:
            return True
        else:
            ball.reflectY() or ball.reflectH()
            return self.collides_with(ball)
