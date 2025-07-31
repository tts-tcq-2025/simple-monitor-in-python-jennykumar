class BatteryManagementSystem:
    def __init__(self, voltage, temperature, soc):
        self.voltage = voltage  # in Volts
        self.temperature = temperature  # in Celsius
        self.soc = soc  # State of Charge in %

    def check_voltage(self):
        if 300 <= self.voltage <= 420:
            return "Voltage OK"
        else:
            return "Voltage Out of Range!"

    def check_temperature(self):
        if 0 <= self.temperature <= 45:
            return "Temperature OK"
        else:
            return "Temperature Out of Range!"

    def check_soc(self):
        if 20 <= self.soc <= 100:
            return "SOC OK"
        else:
            return "SOC Out of Range!"

    def status_report(self):
        return {
            "Voltage": self.check_voltage(),
            "Temperature": self.check_temperature(),
            "SOC": self.check_soc()
        }

