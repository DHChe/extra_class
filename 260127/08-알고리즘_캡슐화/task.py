from abc import ABC, abstractmethod

class VendingMachine:
  def __init__(self, price):
    self.price = price
  
  # 동전 투입
  def coin(self, amount):
    print(f"{amount}를 투입하였습니다.")

  
  def validate_price(self, price)

  @abstractmethod
  def prepared_product(self):
    pass

  def serve_product(self):
    print("제품이 나왔습니다.")

  def return_change(self, )