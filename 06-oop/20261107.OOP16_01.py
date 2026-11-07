'''开发一个会员订单系统，需要根据不同的会员级别和促销活动计算订单的最终价格
创建一个 Discount 类，包含一个类属性 rate，表示折扣率，默认为 0。
实现一个类方法 set_rate(cls, rate)，用于设置折扣率。
实现一个静态方法 calculate(price)，用于根据当前的折扣率计算最终价格。
根据不同的会员级别（如普通会员、黄金会员、白金会员）设置不同的折扣率。'''
class Discount:
    rate = 0
    @classmethod
    def set_rate(cls, rate):
        cls.rate = rate
    @staticmethod
    def calc(price):
        return price * (1 - Discount.rate)

Discount.set_rate(0.2)
original_price = 200
final_price = Discount.calc(original_price)
print(f"原价：{original_price}，折后价：{final_price}")
