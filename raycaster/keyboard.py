from dataclasses import dataclass


@dataclass
class Keyboard:
    A: bool = False
    D: bool = False
    W: bool = False
    S: bool = False
    UP: bool = False
    DOWN: bool = False
    ESCAPE: bool = False
    MOUSE_MOTION: float = 0
