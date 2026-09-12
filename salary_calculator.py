# 个税工资计算器
# 题目：输入员工的月税前工资，按照以下规则计算税后到手工资：
# - 5000元及以内：不扣税
# - 超过5000至8000部分：扣3%
# - 超过8000至17000部分：扣10%
# - 超过17000至30000部分：扣20%
# - 超过30000部分：扣25%
# 输出税前工资、扣税金额、税后工资，保留2位小数。
# 考察点：变量运算、if-elif-else分支、格式化输出、业务逻辑拆解
# 进阶挑战：加入五险一金计算（社保10.5%，公积金7%，基数上限30000），先扣五险一金再算个税。

# input_salary = float(input("请输入您的工资："))
# if input_salary <= 5000:
#     print(f"税前工资：{input_salary} 扣税金额：{0} 税后工资：{input_salary}")
# elif input_salary > 5000 and input_salary <= 8000:
#     print(f"税前工资：{input_salary} 扣税金额：{input_salary * 0.03} 税后工资：{input_salary * 0.97}")
# elif input_salary > 8000 and input_salary <= 17000:
#     print(f"税前工资：{input_salary} 扣税金额：{input_salary * 0.1} 税后工资：{input_salary * 0.9}")
# elif input_salary > 17000 and input_salary <= 30000:
#     print(f"税前工资：{input_salary} 扣税金额：{input_salary * 0.2} 税后工资：{input_salary * 0.8}")
# else:
#     print(f"税前工资：{input_salary} 扣税金额：{input_salary * 0.25} 税后工资：{input_salary * 0.75}")

from decimal import Decimal
salary = Decimal(input("请输入税前月工资（元）："))

# 参数设置
social_rate = Decimal("0.105")    # 社保比例10.5%
fund_rate = Decimal("0.07")       # 公积金比例7%
insurance_base_max = Decimal("30000") # 五险一金基数上限
tax_threshold = Decimal("5000")   # 个税起征点

# 确定五险一金缴费基数，超过3万按3万算
base = salary
if base > insurance_base_max:
    base = insurance_base_max

# 计算五险一金总扣除
insurance = base * social_rate
fund = base * fund_rate
five_one_total = insurance + fund

# 扣除五险一金后的收入
after_insurance = salary - five_one_total
taxable_income = after_insurance - tax_threshold
tax = Decimal("0")

# 阶梯个税计算
if taxable_income > 0:
    if taxable_income <= 3000:
        tax = taxable_income * Decimal("0.03")
    elif taxable_income <= 12000:
        tax = Decimal("3000") * Decimal("0.03") + (taxable_income - Decimal("3000")) * Decimal("0.1")
    elif taxable_income <= 25000:
        tax = Decimal("3000") * Decimal("0.03") + Decimal("9000") * Decimal("0.1") + (taxable_income - Decimal("12000")) * Decimal("0.2")
    else:
        tax = Decimal("3000") * Decimal("0.03") + Decimal("9000") * Decimal("0.1") + Decimal("13000") * Decimal("0.25") + (taxable_income - Decimal("25000")) * Decimal("0.25")

final_salary = after_insurance - tax

# quantize 设置保留2位小数，金额专用
two_decimal = Decimal('0.00')
insurance = insurance.quantize(two_decimal)
fund = fund.quantize(two_decimal)
five_one_total = five_one_total.quantize(two_decimal)
tax = tax.quantize(two_decimal)
final_salary = final_salary.quantize(two_decimal)

print(f"税前工资：{salary} 元")
print(f"社保扣除：{insurance} 元")
print(f"公积金扣除：{fund} 元")
print(f"五险一金合计扣除：{five_one_total} 元")
print(f"个税扣除：{tax} 元")
print(f"最终到手工资：{final_salary} 元")