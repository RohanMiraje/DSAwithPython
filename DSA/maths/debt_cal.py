principal = 400000
roi = 1.5


def get_interest():
    net_int = 0
    outstanding = principal
    fix_contribution = 15000
    for i in range(36):
        if outstanding > 0:
            paid_int = outstanding * (roi / 100)
            contri = fix_contribution
            contri -= paid_int
            outstanding -= contri
            net_int += paid_int
    return net_int, outstanding


def emi_calculator(loan_amount, no_of_years, roi):
    # [P.r.(1+r)^n/ (1+r)^n-1]
    p = loan_amount
    n = no_of_years
    r = roi
    emi = (p * r) * (1 + r) ** n / ((1 + r) ** n) - 1
    return emi


if __name__ == '__main__':
    print(f"{get_interest()}")
    print(f"{emi_calculator(150000, 2, 16.75)}")
