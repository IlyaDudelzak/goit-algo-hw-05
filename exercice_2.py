def generator_numbers(text: str):
  for n in text.split():
    try:
      yield float(n.strip())
    except Exception:
      pass

def sum_profit(text: str, func):
  sum = 0
  for n in func(text):
    sum += n
  return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")