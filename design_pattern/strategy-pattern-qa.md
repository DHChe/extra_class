# Strategy Pattern 발표 예상 질문 & 답변
> 헤드퍼스트 디자인패턴 - SimUDuck 오리 시뮬레이션 게임 기반

---

## OOP 기본 개념 관련 질문

### Q1. "데이터의 무결성"을 보장한다는 게 무슨 의미인가요?

**A:** 데이터 무결성(Data Integrity)이란 데이터가 정확하고 일관된 상태를 유지하는 것을 의미합니다.

SimUDuck 게임에서의 예시:

```python
class Duck:
    def __init__(self):
        self.__fly_behavior = None  # private 변수
    
    def set_fly_behavior(self, behavior):
        if behavior is None:
            raise ValueError("행동은 None이 될 수 없습니다")
        if not isinstance(behavior, FlyBehavior):
            raise TypeError("FlyBehavior 타입이어야 합니다")
        self.__fly_behavior = behavior
```

- 만약 `fly_behavior`가 외부에서 직접 수정 가능하다면, 잘못된 타입이나 None이 설정될 수 있습니다.
- 캡슐화를 통해 메서드로만 값을 변경하게 하면, 유효성 검사를 거쳐 **항상 올바른 상태**를 유지할 수 있습니다.

---

### Q2. "핵심 인터페이스"가 무엇인가요?

**A:** 인터페이스란 객체가 외부와 소통하는 창구, 즉 **"무엇을 할 수 있는가"를 정의한 것**입니다.

SimUDuck에서의 예시:
- 핵심 인터페이스: `fly()`, `quack()`, `display()`, `swim()`
- 숨겨진 내부 구현: 어떤 방식으로 나는지, 어떤 소리를 내는지

사용자(개발자)는 오리가 어떻게 나는지 내부 구현을 몰라도 `duck.fly()`만 호출하면 됩니다. 이것이 바로 추상화를 통해 **핵심 인터페이스만 노출**하는 것의 장점입니다.

---

### Q3. 클래스와 객체의 차이점은 무엇인가요?

**A:** 
| 클래스 (Class) | 객체 (Object) |
|---------------|--------------|
| 설계도, 템플릿 | 실제로 만들어진 실체 |
| 메모리에 올라가지 않음 | 메모리에 할당됨 |
| 하나만 존재 | 여러 개 생성 가능 |

```python
# 클래스 = 오리를 만드는 설계도
class MallardDuck(Duck):
    def display(self):
        print("저는 청둥오리입니다")

# 객체 = 실제 오리들
duck1 = MallardDuck()  # 청둥오리 1
duck2 = MallardDuck()  # 청둥오리 2
duck3 = RubberDuck()   # 고무오리
```

---

### Q4. 인스턴스(Instance)란 무엇인가요?

**A:** 인스턴스는 클래스로부터 생성된 **구체적인 객체**를 말합니다. 객체와 거의 같은 의미로 사용됩니다.

- "객체"는 일반적인 개념
- "인스턴스"는 특정 클래스와의 관계를 강조할 때 사용

```python
mallard = MallardDuck()
# mallard는 MallardDuck 클래스의 "인스턴스"
# mallard는 Duck의 "객체"
```

---

### Q5. 캡슐화와 추상화의 차이점은 무엇인가요?

**A:**

| 캡슐화 (Encapsulation) | 추상화 (Abstraction) |
|----------------------|---------------------|
| **어떻게** 숨길 것인가 | **무엇을** 보여줄 것인가 |
| 구현 세부사항을 **숨기는 기법** | 복잡성을 줄이고 **핵심만 추출** |
| 데이터 보호가 목적 | 설계 단순화가 목적 |

SimUDuck 비유:
- **추상화**: Duck 클래스에서 `fly()`, `quack()` 메서드만 정의 (무엇을 할 수 있는지)
- **캡슐화**: `FlyBehavior` 객체를 private으로 숨기고 `setFlyBehavior()`로만 변경 가능하게 함

---

### Q6. Low Coupling(낮은 결합도)이 왜 중요한가요?

**A:** Coupling(결합도)은 모듈 간의 의존성 정도를 나타냅니다.

**SimUDuck에서 High Coupling의 문제점:**
```python
# High Coupling (나쁜 예) - Duck 클래스 안에 직접 구현
class Duck:
    def fly(self):
        print("날개로 날아갑니다")  # 모든 오리가 이렇게 날아야 함
```
- RubberDuck이 추가되면 Duck 클래스를 수정해야 함
- 새로운 나는 방식이 추가될 때마다 코드 수정 필요

**Low Coupling의 장점 (Strategy Pattern 적용):**
```python
# Low Coupling (좋은 예) - 행동을 분리
class Duck:
    def __init__(self):
        self.fly_behavior = None  # 어떤 FlyBehavior든 주입 가능
    
    def perform_fly(self):
        self.fly_behavior.fly()
```
- Duck과 FlyBehavior가 느슨하게 연결
- 새로운 나는 방식 추가 시 Duck 코드 수정 불필요

---

### Q7. 메서드(Method)와 함수(Function)의 차이점은 무엇인가요?

**A:**

| 함수 (Function) | 메서드 (Method) |
|----------------|----------------|
| 독립적으로 존재 | 클래스 안에 정의 |
| `function_name()` | `object.method_name()` |
| 객체 상태에 접근 불가 | 객체의 속성에 접근 가능 |

```python
# 함수 - 독립적
def make_sound(sound):
    print(sound)

# 메서드 - Duck 클래스 안에서 정의
class Duck:
    def __init__(self):
        self.quack_behavior = None
    
    def perform_quack(self):  # self를 통해 객체 상태 접근
        self.quack_behavior.quack()
```

---

## OOP 4대 요소 관련 질문

### Q8. OOP의 4가지 요소가 무엇인가요? (3, 4번이 빠져있는데요?)

**A:** OOP의 4대 요소는 다음과 같습니다:

1. **캡슐화 (Encapsulation)**: 데이터와 메서드를 묶고, 내부 구현을 숨김
2. **추상화 (Abstraction)**: 핵심 기능만 추출하여 복잡성 감소
3. **상속 (Inheritance)**: 부모 클래스의 속성과 메서드를 자식 클래스가 물려받음
4. **다형성 (Polymorphism)**: 같은 인터페이스로 다른 동작을 수행

---

### Q9. 상속(Inheritance)이란 무엇인가요?

**A:** 상속은 기존 클래스의 속성과 메서드를 **새로운 클래스가 물려받는 것**입니다.

SimUDuck 예시:
```python
class Duck:
    def swim(self):
        print("모든 오리는 물에 뜹니다")
    
    def display(self):
        pass  # 서브클래스에서 구현

class MallardDuck(Duck):  # Duck을 상속
    def display(self):
        print("저는 청둥오리입니다")

class RedheadDuck(Duck):  # Duck을 상속
    def display(self):
        print("저는 아메리카흰죽지입니다")
```

**SimUDuck에서 상속의 한계:**
- `fly()` 메서드를 Duck에 추가하면 모든 서브클래스가 상속받음
- RubberDuck도 날게 되는 문제 발생!

---

### Q10. 다형성(Polymorphism)이란 무엇인가요?

**A:** 다형성은 **같은 인터페이스(메서드)를 호출해도 객체에 따라 다르게 동작**하는 것입니다.

SimUDuck에서의 다형성:
```python
# FlyBehavior 인터페이스
class FlyBehavior:
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("날개로 날아갑니다!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("저는 날 수 없어요")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("로켓 추진으로 날아갑니다!")

# 다형성 활용 - 같은 fly() 호출, 다른 결과
behaviors = [FlyWithWings(), FlyNoWay(), FlyRocketPowered()]
for behavior in behaviors:
    behavior.fly()
```

---

## SimUDuck 오리 시뮬레이션 관련 질문

### Q11. SimUDuck이 무엇인가요?

**A:** SimUDuck은 헤드퍼스트 디자인패턴 책에 나오는 **오리 연못 시뮬레이션 게임 회사**입니다.

- 다양한 오리 종류가 헤엄치고, 꽥꽥거리는 게임
- 초기에는 표준 OOP 기법(상속)을 사용하여 설계
- 경쟁사와의 차별화를 위해 "오리가 날 수 있는 기능" 추가 요청
- 이 과정에서 상속의 한계를 발견하고 Strategy Pattern을 도입

---

### Q12. SimUDuck에서 처음에 어떤 문제가 발생했나요?

**A:** 임원진이 "오리가 날 수 있어야 한다"고 요청하여 Duck 슈퍼클래스에 `fly()` 메서드를 추가했습니다.

**문제 상황:**
```
Duck (슈퍼클래스)
├── quack()
├── swim()
├── display()  ← 추상 메서드
├── fly()      ← 새로 추가! 모든 서브클래스가 상속
│
├── MallardDuck   ← 날 수 있음 ✓
├── RedheadDuck   ← 날 수 있음 ✓
├── RubberDuck    ← 고무오리가 날아다님! ✗
└── DecoyDuck     ← 나무 모형오리가 날아다님! ✗
```

**결과:** 고무 오리(RubberDuck)와 나무 모형 오리(DecoyDuck)까지 날아다니게 됨!

---

### Q13. 첫 번째 해결 시도는 무엇이었나요? 왜 실패했나요?

**A:** **메서드 오버라이드(재정의)**를 시도했습니다.

```python
class RubberDuck(Duck):
    def fly(self):
        pass  # 아무것도 하지 않음 (날지 않음)
    
    def quack(self):
        print("삑삑!")  # 고무오리는 꽥꽥이 아닌 삑삑
```

**실패 이유:**
1. **유지보수 악몽**: 새로운 오리 추가할 때마다 fly()와 quack()을 오버라이드해야 할지 판단 필요
2. **코드 중복**: 날지 못하는 오리가 10종류면 10번 오버라이드
3. **확장성 문제**: 새로운 행동(예: rocket fly)이 추가되면 모든 클래스 검토 필요
4. **실수 가능성**: 오버라이드를 깜빡하면 버그 발생

---

### Q14. 두 번째 해결 시도(인터페이스)는 왜 실패했나요?

**A:** `Flyable`과 `Quackable` 인터페이스를 만들어서 필요한 오리만 구현하게 했습니다.

```python
class Flyable:
    def fly(self):
        pass

class Quackable:
    def quack(self):
        pass

class MallardDuck(Duck, Flyable, Quackable):
    def fly(self):
        print("날개로 날아갑니다")  # 직접 구현해야 함
    
    def quack(self):
        print("꽥꽥!")  # 직접 구현해야 함
```

**실패 이유:**
1. **코드 재사용 불가**: 인터페이스는 구현을 가질 수 없음
2. **코드 중복**: 48개의 Duck 서브클래스가 있다면, 나는 오리마다 동일한 fly() 코드를 각각 작성해야 함
3. **변경의 어려움**: 나는 방식을 바꾸려면 모든 관련 클래스를 수정해야 함

> "코드 재사용이라는 상속의 장점을 완전히 잃어버림"

---

### Q15. Strategy Pattern으로 어떻게 해결했나요?

**A:** **"변하는 부분을 캡슐화하라"** 원칙을 적용했습니다.

**변하는 것과 변하지 않는 것 분리:**
- 변하지 않는 것: `swim()`, `display()` → Duck 클래스에 유지
- 변하는 것: `fly()`, `quack()` → 별도 클래스로 분리

**해결 구조:**
```python
# 나는 행동 인터페이스
class FlyBehavior:
    def fly(self): pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("날개로 날아갑니다!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("저는 날 수 없어요")

# 꽥꽥거리는 행동 인터페이스
class QuackBehavior:
    def quack(self): pass

class Quack(QuackBehavior):
    def quack(self):
        print("꽥꽥!")

class Squeak(QuackBehavior):
    def quack(self):
        print("삑삑!")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("...")  # 소리 못냄

# Duck 클래스
class Duck:
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None
    
    def perform_fly(self):
        self.fly_behavior.fly()
    
    def perform_quack(self):
        self.quack_behavior.quack()
    
    def set_fly_behavior(self, fb):
        self.fly_behavior = fb  # 런타임에 행동 변경!
```

---

### Q16. Strategy Pattern의 핵심 디자인 원칙은 무엇인가요?

**A:** 헤드퍼스트에서 제시하는 3가지 디자인 원칙:

1. **애플리케이션에서 달라지는 부분을 찾아내고, 달라지지 않는 부분과 분리한다**
   - fly()와 quack()은 오리마다 다름 → 분리
   - swim()은 모든 오리가 동일 → Duck 클래스에 유지

2. **구현보다는 인터페이스에 맞춰서 프로그래밍한다**
   - Duck은 FlyBehavior 인터페이스에만 의존
   - 구체적인 FlyWithWings, FlyNoWay는 모름

3. **상속보다는 구성(Composition)을 활용한다**
   - "A는 B이다" (is-a) 보다 "A에는 B가 있다" (has-a)
   - Duck에는 FlyBehavior가 있다

---

### Q17. 런타임에 행동을 바꿀 수 있다는 게 무슨 의미인가요?

**A:** 프로그램 실행 중에 오리의 행동을 동적으로 변경할 수 있다는 의미입니다.

```python
# 모형 오리 생성 (처음엔 날 수 없음)
model_duck = ModelDuck()
model_duck.fly_behavior = FlyNoWay()
model_duck.perform_fly()  # "저는 날 수 없어요"

# 로켓 추진 장치 장착! (런타임에 행동 변경)
model_duck.set_fly_behavior(FlyRocketPowered())
model_duck.perform_fly()  # "로켓 추진으로 날아갑니다!"
```

**상속과의 차이:**
- 상속: 컴파일 시점에 행동이 고정됨
- Strategy Pattern: 실행 중에 행동 교체 가능

---

### Q18. Strategy Pattern은 언제 사용하나요?

**A:** 다음과 같은 상황에서 유용합니다:

1. **여러 알고리즘 중 선택이 필요할 때**
   - SimUDuck: 여러 나는 방식 중 선택 (날개, 로켓, 안 날기)
   - 결제 방식: 카드, 현금, 포인트

2. **런타임에 행동을 변경해야 할 때**
   - SimUDuck: 오리에게 로켓 추진 장치 장착
   - 게임 캐릭터의 무기 교체

3. **조건문(if-else)이 많아질 때**
   - 조건문 대신 Strategy 객체로 대체

4. **유사한 클래스가 행동만 다를 때**
   - SimUDuck: MallardDuck, RubberDuck 등 행동만 다름

---

### Q19. Strategy Pattern의 장점과 단점은 무엇인가요?

**A:**

**장점:**
- 알고리즘을 독립적으로 변경 가능
- 런타임에 행동 교체 가능
- 조건문 감소로 코드 가독성 향상
- Open-Closed Principle 준수 (확장에 열림, 수정에 닫힘)
- 코드 재사용 (FlyWithWings를 여러 오리가 공유)

**단점:**
- 클래스 수가 증가 (FlyBehavior, QuackBehavior 등)
- 클라이언트가 Strategy 종류를 알아야 함
- 간단한 경우 오히려 복잡해질 수 있음

---

### Q20. 상속 대신 Strategy Pattern(구성)을 사용하는 이유는?

**A:** 

| 상속 (Inheritance) | Strategy Pattern (구성) |
|-------------------|------------------------|
| 컴파일 타임에 행동 결정 | 런타임에 행동 변경 가능 |
| 부모 변경 시 자식 영향 | 독립적으로 변경 가능 |
| "is-a" 관계 | "has-a" 관계 |
| 단일 상속 제한 | 여러 전략 조합 가능 |
| 코드 중복 발생 | 전략 객체 재사용 |

> **원칙**: "상속보다는 구성(Composition)을 활용한다"

SimUDuck에서:
- ❌ "MallardDuck은 FlyWithWings**이다**" (is-a)
- ✅ "MallardDuck은 FlyWithWings**를 가진다**" (has-a)

---

## 추가 심화 질문

### Q21. Design Pattern을 왜 배워야 하나요?

**A:**
1. **공통 어휘 제공**: 개발자 간 소통이 쉬워짐 ("여기 Strategy Pattern 적용하죠")
2. **검증된 솔루션**: 선배 개발자들이 이미 검증한 해결책
3. **유지보수성 향상**: 코드 구조가 명확해짐
4. **재사용성 증가**: 패턴을 알면 유사 문제에 적용 가능

---

### Q22. SOLID 원칙과 Strategy Pattern의 관계는?

**A:** Strategy Pattern은 SOLID 원칙 중 여러 가지를 만족합니다:

- **S (Single Responsibility)**: 각 Strategy 클래스는 하나의 알고리즘만 담당
  - FlyWithWings는 날개로 나는 것만 담당
- **O (Open-Closed)**: 새 Strategy 추가 시 기존 코드 수정 불필요
  - FlyRocketPowered 추가해도 Duck 클래스 수정 없음
- **L (Liskov Substitution)**: 모든 Strategy는 동일한 인터페이스로 대체 가능
  - FlyBehavior 자리에 어떤 구현체든 사용 가능
- **D (Dependency Inversion)**: 구체 클래스가 아닌 인터페이스에 의존
  - Duck은 FlyBehavior 인터페이스에만 의존

---

### Q23. 실무에서 Strategy Pattern이 사용되는 예시는?

**A:**
1. **결제 시스템**: 카드결제, 계좌이체, 간편결제 등
2. **인증 방식**: OAuth, JWT, Session 등
3. **파일 압축**: ZIP, RAR, 7z 알고리즘
4. **데이터 검증**: 이메일 검증, 전화번호 검증 등
5. **할인 정책**: 정률 할인, 정액 할인, 쿠폰 할인 등
6. **정렬 알고리즘**: 상황에 따라 다른 정렬 방식 선택
7. **로깅 시스템**: 콘솔 로깅, 파일 로깅, 원격 로깅 등
