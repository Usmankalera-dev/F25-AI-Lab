# Lab 3: Model-Based Reflex Agent


class TemperatureAgent:
    def __init__(self):
        self.heater = False
        self.ac = False

    def act(self, temperature):
        if temperature < 20 and self.heater == False:
            self.heater = True
            print(temperature, "C: Heater ON")
        elif temperature >= 20 and self.heater == True:
            self.heater = False
            print(temperature, "C: Heater OFF")
        else:
            print(temperature, "C: No heater change")

        if temperature > 26 and self.ac == False:
            self.ac = True
            print(temperature, "C: AC ON")
        elif temperature <= 26 and self.ac == True:
            self.ac = False
            print(temperature, "C: AC OFF")
        else:
            print(temperature, "C: No AC change")


temperatures = [18, 22, 25, 25, 19]
agent = TemperatureAgent()

for temperature in temperatures:
    agent.act(temperature)
