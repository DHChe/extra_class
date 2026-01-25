# 1. OOP(Object-oriented programming)

OOP는 객체 지향 프로그래밍으로 객체 개념을 기반으로 하는 컴퓨터 프로그래밍의 패러다임이다. 

컴퓨터 프로그래밍에서 작게 구분하는 단위는 **클래스**이고, 이러한 클래스를 활용해 코딩을 하는 것을 **객체 지향형 프로그래밍**이라고 한다. 

즉 클래스는 객체를 생성하기 위한 템플릿의 역할을 한다.

>## Class / Object / Method
>
>- 클래스는 같은 종류(또는 문제해결을 위한) 집단에 속하는 속성(**attribute**)과 행위(**behavior**)를 정의한것
>- 객체는 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다. 객체는 자기자신의 고유의 속성(**attribute**)을 가지고 클래스에서 정의한 행위(**behavior**)를 할 수 있다.
>    - 이때 객체의 행위는 클래스에 정의된 행위에 대한 정의를 공유함으로써 메모리를 경제적으로 사용
>- 메서드는 클래스로부터 생성된 객체를 사용하는 방법으로서 객체에 명령을 내리는 메세지


> ## OOP의 요소
>1. `캡슐화 (Encapsulation)`: 객체의 속성(***data field***)과 행위(***method***)를 하나로 묶고, 실제 구현 내용일부를 내부에 감추어 은닉한다.
>- 객체를 외부에서 수정하지 못하게 하여 데이터의 ***무결성***을 보장한다. 
>- 내부 로직이 변경되어도 외부 코드에는 영향을 주지 않아 low coupling 효과가 있다.
>2. `추상화 (Abstraction)`: 사용자에게 필요한 핵심 인터페이스(기능)만을 추출하여 정의하는 과정
>- 복잡성을 낮추어 사용자가 **어떻게**가 아닌 **무엇을** 하는지에 집중하게 하여 ***설계의 명확성***을 높임
>3. `상속 (Inheritance)`: superClass의 특성과 기능을 물려받아 새로운 subClass를 생성하는것
>- 공통된 로직은 superClass에게 집중시켜 **코드 재사용성**을 극대화
>4. `다형성 (Polyporphism)`: 하나의 인터페이스, 클래스가 객체로 동작할 수 있는 능력
>- 오버라이딩, 오버로딩을 통해 구현되며 구체적 타입에 의존하지 않고 추상적 타입에 의존하여 유연성과 확장성을 향상시킴

<div style="height: 50px;"></div>

# 2. 문제의 발단(오리 시뮬레이션 게임)
## 2.1 초기 설계 <span id="s-1"></span>

➡️ 초기 설계는 단순한 상속에서 시작  
```python
# 수퍼클래스(Ducks)
class Ducks:
    # 오리가 가지는 기본적 행동
    def quack(self):
        print("꽥")

    def swim(self):
        print("물위에서 떠다니며 수영합니다.")

    # 오리마다 외형이 다르므로 상속받는 서브클래스에서 직접구현하도록 하는 추상화
    def appearance(self):
        pass
```
```python
# 서브 클래스
# Ducks 슈퍼클래스를 상속하므로 기본적으로 quack, swim을 물려받음
class MallardDuck(Ducks):

    # 추상화를 개별적으로 구현
    def appearance(self):
        print("귀엽게 생긴 청둥오리입니다.")

class RedheadDuck(Ducks):
    def appearance(self):
        print("무섭게 생긴 빨간머리오리입니다.")

class RubberDuck(Ducks):
    def display(self):
        print("말랑말랑 고무오리입니다")

    def quack(self):
        
        # 다른 울음소리를 오버라이딩
        print("삑삑")

    def flying(self):

        # 날지 못하는 오버라이딩
        print("저는 날지 못합니다.")

class DecoyDuck(Ducks):
    def display(self):
        print("딱딱한 나무오리입니다")

    def quack(self):
        
        # 울지 못해 pass로 기능을 지움
        pass

    def flying(self):

        # 날지 못해 pass로 기능을 지움
        pass
```
<br> 

➡️ 요청사항(behavior) 1️⃣: 나는 행동(flying)추가 요청을 부모클래스에 직접 추가
```python
class Ducks:
    # ...

    # 부모 클래스에 나는 행동을 구현함
    def flying(self):
        print("퍼덕퍼덕 날아갑니다.")

    # ...
```

## 2.2 문제의 발생(상속 구조의 결함)
[2.1 초기 설계](#s-1)에서 오리는 공통된 quack과 swim을 가지고 있도록 설계되었다.  
appearance는 오리마다 다르기에 서브클래스에서 직접 구현하도록 구현하였다. 또한 **RubberDuck과 DecoyDuck의 경우 오버라이딩** 하였다.  

그 후에 새로운 행동 flying이 추가되었을때 부모 클래스에 구현하였는데 날지 못하여야 하는 RubberDuck과 DecoyDuck이 날라다니는 문제가 발생했다. 
일부 클래스만 적용되어야 하는 메소드임을 잊고 부모 클래스에 구현하는 바람에 상속받는 전체 오리가 날라다니는 문제가 발생한 것이다.  
여기서 발생하는 문제들이 있다.

<br>

`유지 보수의 문제발생`
- RubberDuck과 DecoyDuck의 경우와 같은 날지 못하는 오리가 100종류라면 오버라이딩을 100번 붙여넣어야 한다.  
문구를 바꾸려면 또 다시 100번을 작업해야 한다. 코드의 재사용성이 사라진다.
- 이제부터는 부모 클래스에 메서드하나가 추가될때마다 그 메서드를 받으면 안되는 자식 클래스가 있는지 하나하나 찾아서 오버라이딩으로   
막아야 하는 문제가 생긴다.

`정적 오버라이딩 문제`
- 상속을 통한 오버라이딩은 정적(statuc)이어서 Runtime 도중 바꿀수 없다.  
실행 중 행동을 바꾸려면 새로운 객체를 새로 만들어 교체해야 하며 이는 객체지향의 유연성을 상실한다.

`유연성(***inflexibility)문제`  
- 상속 구조는 부모의 메서드 변화를 상속받는 자식에게 강한 제약을 함으로써 RubberDuck이나 DecoyDuck과 같은 예외 상황에서  
유연하게 대처하지 못하고 전체 시스템에 문제를 일으킬 수 있다. 

`LSP(Liskov substitution principle, 리스코프 치환 원칙) 위반 가능성`
- 부모 클래스가 할 수 있는 일은 자식 클래스도 똑같이 할 수 있어야 한다.
- Ducks.flying()이 호출 될때 RubberDuck과 같은 객체라면 예상치 못한 동작(오류)가 발생
- 자식이 부모의 메소드를 옳게 수행하지 못하면서 **다형성의 신뢰도**가 깨짐

단순 인터페이스 상속<span id="s-2"></span>
```python
# Joe는 flyable과 quackable 인터페이스를 구현하려고 했으나 방식은 여전히 문제
# flyable과 같은 단순 인터페이스 상속은 날 수 있는 오리들만 이 flyable 인터페이스를 구현하게 하는 것인데
# 이 인터페이스는 메서드 이름만 결정하고 실제 구현은 상속받은 클래스에서 직접 구현해야 하므로
# 여전히 자식 클래스에서 코드 중복과 유지보수의 문제가 발생

from abc import ABC, abstractmethod

# 1. 추상 베이스 클래스 상속: Python에서는 자바와 달리 abc 모듈의 ABC를 사속받고 @abstractmethod를 선언해야
# 자식 클래스에서 구현을 강제할 수 있음.
class Flyable(ABC):
    @abstractmethod
    def flying(self):
        pass

class Quackable(ABC):
    @abstractmethod
    def quack(self):
        pass

# 2. 서브 클래스에서 직접 인터페이스를 상속하여 구현
class MallardDuck(Flyable, Quackable):
    # ...
    def flying(self):
        print("퍼덕퍼덕 날아갑니다")

    def quackabe(self):
        print("꽥")


```

<br>

# 3. 문제 해결을 위한 설계
## 3.1 프로그래밍에서의 변화
변화를 인식해야 한다.  
시간에 흐름에 따라 변화는 필연적으로 연결된다.  
소프트웨어 개발에 한정하자면 
- 사용자의 요청이 변화할 수도
- 새로운 요청이 생길 수도

따라서 이러한 변화에 어떻게 대응할 수 있을지를 고민 할 수 있어야 한다. 단순히 상속이 나쁘다는 것이 아니라 **변화**에  
어떻게 대응할 것인가 하는 문제이다.

## 3.2 문제점을 정확히 파악
여기서 반드시 알아야 할 점은 상속 그 자체의 결함이 아니라 앞서 서술한 바와 같이 **'변화하는 부분을 변하지 않는 내부 속성에 강제로 고착화 시킨 `경직성`에 있다.'**  
이와 같이 어느 특정의 방법이 그 자체의 결함이나 설계에 문제를 발생시킨다는 것이 아니라는 것을 인지하고 문제점을 명확히 하여 설계하여야 한다. 

## 3.3 바뀌는 부분과 그렇지 않은 부분 분리하기
> ### "바뀌는 부분은 따로 뽑아서 캡슐화한다. 그러면 나중에 바뀌지 않는 부분에는 영향을 미치지 않고 그 구분만 고치거나 확장할 수 있다."  
- 꺼낸것들은 별도의 클래스 집합으로
- 그리고 다양한 메소드를 구현해둠

## 3.4 구현이 아닌 인터페이스에 맞춰 프로그래밍한다.
Program to an interface, not an implementation.  
여기서 Interface의 갠념은 `상위 형식(Supertype)`에 맞추어 프로그래밍한다는 개념을 내포한다.  
> ### Python은 동적 언어라 타닙 제한이 없지만, Type Hinting을 활용해 자바처럼 상위 형식에 의존한다는 설계를 명확히 할 수 있다.

[2.1 초기 설계](#s-1)와 [단순 인터페이스 상속](#s-2)에서는 클래스 내부에 고착화 하는 설계를 하였는데 이를 `구현에 맞춘 설계`라 볼수 있다. 이는 실행중 변경이 힘들고, 새로운 행동이 추가될 때 기존 코드를 수정해야 하는 문제가 있다.  

쉽게 말하자면 특정 구현(제품)에 맞춰지는 설계라 할 수 있는데 예를 들면 TV를 벽면에 설치할때 나중에 TV를 다른 제품으로 교체할 `변화`를 염두하지 않고, 벽면에 특정 제품에만 딱 맞는 TV를 설치하는 꼴이라 할 수 있다.  

**핵심**은 실제 실행시 사용되는 객체가 코드에 고정되지 않도록 상위 형식(supertuype)에 맞추어 `다형성`을 활용해야 한다는 것이다.  
이때 파이썬에서는 `__init__`생성자에서 객체를 인수로 받아 저장하는 **구성(Composition)** 방식을 사용하는데 이때 Type Hinting으로 상위형식에 의존한다는 의도를 드러낼 수 있다.

### 3.4.1 오리의 행동 구현  
<br>
행동에 대한 인터페이스 정의

```python
from abc import ABC, abstractmethod

class FlyBehavior(ABC): # 날 수 있는 클래스는 이 인터페이스를 구현해야 함
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC): # 우는 행동에 대한 인터페이스
    @abstractmethod
    def quack(self):
        pass

```
<br>
구체적 행동을 구현하는 클래스

```python
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("퍼덕퍼덕 날개로 날아갑니다.")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("날 수 없습니다.")

class Quack(QuackBehavior):
    def quack(self):
        print("꽥꽥")

class RubberQuack(QuackBehavior):
    def quack(self):
        print("삑삑")
```
### 3.4.2 오리의 행동 통합하기
<br>
오리 클래스(또는 그 서브클래스)에서 메소드로 구현하지 않고 다른 클래스에 위임

```python
from abc import ABC, abstractmethod

class Ducks(ABC):
    def __init__(self):

        self.fly_behavior: FlyBehavior = None
        slef.quack_bahavior: QuackBehavior = None

    def perform_quack(slef):
        # 직접 우는 소리를 처리하지 않고 객체에 위임
        self.quack_behavior.quack()

    def perform_fly(self):
        # 직접 날아가는 방법을 처리하지 않고 객체에 위힘
        self.fly_behavior.fly()

    def swim(self):
        # 모든 공통된 것은 여기서 직접 구현
        print("오리라면 모두 물위에서 수영을 합니다.")

    # 외모는 오리마다 반드시 다르다는 가정하에 객체가 각자 구현하도록 강제
    @abstractmethod
    def appearance(self):
        pass
```

1. FlyBehavior라는 인터페이스는 아무일도 하지 않는다. 단지 "나를 상속받는 모든 클래스는 반드시 fly라는 이름의 함수를 가져야 한다."고 `@abstractmethod`로 강제하고 있다. 따라서 `.fly()` 만 호출하면 동작하게 된다.

2. FlyWithWings 클래스는 실제 "퍼덕퍼덕 날개로 날아갑니다"라는 실행로직을 메모리에 올리고 대기하고 있다.

3. Ducks 클래스는 변수를 확보:  
연결 지점으로서 객체를 담을 변수 `self.fly_behavior` 변수를 빈값으로 준비.  
그 객체에게 일을 시킬 메서드 `perform_fly`만 준비

4. 실제 조립
```python
class MallardDuck(Duck):
    def __init__(self):
        # 부모의 __init__ 구조를 사용
        super().__init__()
        # FlyWithWings 객체의 주소를 fly_behavior 변수에 대입
        # 여기서 self가 behavior들과 물리적 결합
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def appearance(self):
        print("청둥청둥 청둥오리입니다.")
```

<div style="height: 50px;"></div>

# 전체 코드 설계
- 행동관련 인터페이스
```python
from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
```
- 구상 클래스
```python

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("퍼덕퍼덕 날개로 힘차게 날아갑니다.")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("저는 날지 못합니다.")

class Quack(QuackBehavior):
    def quack(self):
        print("꽥꽥!")

class Squeak(QuackBehavior):
    def quack(self):
        print("삑삑!")
```
- 슈퍼클래스(연결, 위임의 본체)
```python
class Duck(ABC):
    def __init__(self):
        self.fly_behavior: FlyBehavior = None
        self.quack_behavior: QuackBehavior = None

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    @abstractmethod
    def appearance(self):
        pass
```
- 서브 클래스(실제 조립)
```python
class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def appearance(self):
        print("청둥청둥 청둥오리입니다.")
```
# 4. 전략 패턴의 적용
## 4.1 동적 행동 지정하기
- Duck 클래스에 새로운 수정자(setter)메서드를 추가
```python
class Ducks(ABC):
    # ...

    # 동적 행동을 위한 메서드
    def set_fly_behavior(self, fb: FlyBehavior):
        # 실행 중에 self.fly_behavior의 내용을 fb로 바꿉니다.
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    # ...
    
    # 위 두 메소드를 호출하면 언제든지 오리의 행동을 바꿀 수 있음.
```
- 초기에 날지 못하는 모형 오리 클래스
```python
class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()
    
    def appearance(self):
        print("가만가만 모형오리입니다")
```
- 로켓을 단 구상 클래스를 새롭게 선언
```python
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("로켓을 달고 날아갑니다.")
```
- 실행 중 행동 변경(Dynamic Change): 런타임에 중 오리는 날 수 있음
```python
# 메인 실행부
if __name__ == "__main__":
    # 청둥오리 테스트
    mallard = MallardDuck()
    mallard.perform_quack() # 꽥꽥
    mallard.perform_fly() # 퍼덕퍼덕 날개로 힘차게 날아갑니다.

    # 모형 오리 
    model = ModelDuck()

    model.perform_fly() # self.fly_behavior = FlyNoWay() - ""저는 날지 못합니다." 출력

    # 런타임 중 행동 교체
    model.set_fly_behavior(FlyRocketPowered())

    # 다시 시도
    model.perform_fly() # 로켓을 달고 날아갑니다. 출력
```
## 4.2 두 클래스를 합치는 방법
> `상속보다는 구성을 활용한다.`  

Duck에는 FlyBehavior와 QuackBehavior가 있다. 이러한 두 클래스를 합치는 것을 `구성(composition)`이라고 한다.  
클래스의 집합 set으로 캡슐화 하면 실행 시 행동을 바꿀 수도 있다.  

상속이 "A는 B의 일종이다(IS-A)" 관계라면 구성은 "A는 B를 가지고 있다(HAS-A)" 관계입니다.
- 상속 (IS-A): 청둥오리는 오리의 일종이다. (MallardDuck is a Duck)
- 구성 (HAS-A): 오리는 날기 행동을 가지고 있다. (Duck has a FlyBehavior)

왜 상속보다 구성을 강조할까?
- 상속은 compile 시점에 결정된다. 실행 중 변경할 수 없다. 상속은 코드를 저장하는 순간 Hard-coding되어 런타임 도중 변경할 수 없다. 마치 유전자처럼 고정되어 태어나므로 중간에 변경할 수 없다는 의미.
- 구성(Composition)은 행동을 변수(예: self.quack_behavior)에 담기 때문에 런타임 도중 다른 행동(변수 변경)이라는 명령이 있으면 행동을 변경할 수 있다.
- 구성은 컴파일 시점에 변수가 있다는 사실만 받고 실행 시에 들어오는 변수에 따라 적용되는 **유연함**을 가지고 있다.






