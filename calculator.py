# calculating financial life

R = 0.02

CONSUMPTION_GROWTH = 0.07
INCOME_GROWTH = 0.07
ANNUAL_CAPITAL_YIELD = 0.07
MONTHLY_CAPITAL_YIELD = (1 + ANNUAL_CAPITAL_YIELD ) ** (1/12) - 1

START_ASSET = 70000
START_INCOME = 327 * 12 # 연봉 4500 만원 실수령
START_MONTHLY_CONSUMPTION = 100

YEAR = 10

def main():
    current_capital = START_ASSET
    for y in range(1, YEAR+1):
        before_capital = current_capital
        print(f'{y} 년 뒤 자산 : {current_capital}')
        for m in range(1, 13):
            month_income = (START_INCOME/12) * ((1+INCOME_GROWTH)**y)
            month_consumption = START_MONTHLY_CONSUMPTION * ((1+CONSUMPTION_GROWTH)**y)
            month_difference = month_income - month_consumption
            current_capital *= MONTHLY_CAPITAL_YIELD + 1
            current_capital += month_difference
        print(f'{y} 년 뒤 월급 : {month_income}')
        print(f'{y} 년 뒤 월소비 : {month_consumption}')
        print(f'{y} 년 뒤 자산증가 : {current_capital - before_capital}')
    return current_capital

if __name__ == "__main__":
    print(main() + 12000)
