class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


class Player:
    def __init__(
            self, pos: Point = Point(0, 0), canFly: bool = False
    ) -> None:
        self.pos = pos
        self.canFly = canFly


player_1 = Player(pos=Point(3, 4), canFly=True)

print("위치: ", player_1.pos.x, player_1.pos.y)
print("날 수 있나?: ", player_1.canFly)