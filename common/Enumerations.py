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


class VisitStatusEnum(enum.Enum):
    PendingVerification = 1
    Scheduled = 2
    Canceled = 3
    Completed = 4
    Failed = 5


PropertyTypeEnum = enum.Enum(
    value="PropertyTypeEnum",
    names=[
        ("House", 1),
        ("Commercial Space", 2)
    ]
)


EnergyCertificateEnum = enum.Enum(
    value="EnergyCertificateEnum",
    names=[
        ("A+", 1),
        ("A", 2),
        ("B", 3),
        ("C", 4),
        ("D", 5),
        ("E", 6),
        ("F", 7),
        ("G", 8),
        ("H", 9)
    ]
)
