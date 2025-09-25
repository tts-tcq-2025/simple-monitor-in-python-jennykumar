
def is_in_range(value, min_val, max_val):
  return min_val <= value <= max_val

def is_below_max(value, max_val):
  return value <= max_val

def battery_is_ok(temperature, soc, charge_rate):
  checks = [
    {"name": "Temperature", "value": temperature, "check": is_in_range, "args": (0, 45)},
    {"name": "State of Charge", "value": soc, "check": is_in_range, "args": (20, 80)},
    {"name": "Charge Rate", "value": charge_rate, "check": is_below_max, "args": (0.8,)}
  ]

  for check in checks:
    if not check["check"](check["value"], *check["args"]):
      print(f'{check["name"]} is out of range!')
      return False
  return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)     # all OK
  assert(battery_is_ok(50, 70, 0.7) is False)    # temperature too high
  assert(battery_is_ok(25, 10, 0.7) is False)    # soc too low
  assert(battery_is_ok(25, 70, 0.9) is False)    # charge rate too high
