import enum


class GlassTypeEnum(enum.Enum):
    Single = 1
    Double = 2
    Triple = 3
    Other = 4


class HeatingTypeEnum(enum.Enum):
    Decentralized = 1
    Central = 2
    Other = 3


class PropertyActionEnum(enum.Enum):
    Sale = 1
    Rent = 2
