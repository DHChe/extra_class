from abc import ABC, abstractmethod

# 인터페이스 구현
class WeaponBehavior(ABC):
    @abstractmethod
    def useWeapon(self):
        pass

# 구상 클래스 구현
class KnifeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("칼로 공격합니다.")

class BowBehavior(WeaponBehavior):
    def useWeapon(self):
        print("활로 공격합니다.")

class AxeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("도끼로 공격합니다.")

class SwordBehavior(WeaponBehavior):
    def useWeapon(self):
        print("검으로 공격합니다.")

# 슈퍼클래스
class Character(ABC):
    def __init__(self):
        self.weapon: WeaponBehavior = None

    def performWeapon(self):
        self.weapon.useWeapon()