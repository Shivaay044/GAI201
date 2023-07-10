

employees = [
    {"name":"John","salary":3000,"designation":"developer"},
    {"name":"Emma","salary":4000,"designation":"manager"},
    {"name":"Kelly","salary":3500,"designation":"tester"},
]


def max_salary(employess):
      max = 0
      for el in employees:
            if el.salary > max :
                  max = el.salary
      return max

ans = max_salary(employees)
print(ans)