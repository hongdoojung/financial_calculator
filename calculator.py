# calculating financial life

R = 0.02
CONSUMPTION_GROWTH = 0.1
INCOME_GROWTH = 0.07
MONTHLY_CAPITAL_YIELD = 0.01

START_ASSET = 8000
START_INCOME = 4000
START_MONTHLY_CONSUMPTION = 120

YEAR = 3


def main():
    current_capital = START_ASSET
    for y in range(YEAR):
        print(current_capital)
        for m in range(12):
            month_income = (START_INCOME/12)*((1+INCOME_GROWTH)**y) - START_MONTHLY_CONSUMPTION*((1+CONSUMPTION_GROWTH)**y)
            current_capital *= MONTHLY_CAPITAL_YIELD + 1
            current_capital += month_income
    return current_capital


if __name__ == "__main__":
    print(main())
