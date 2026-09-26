"""Lab 3: model-based reflex agent controlling a heater and air-conditioner."""


class TemperatureAgent:
    """Agent with internal state for heater and air-conditioner."""

    def __init__(self) -> None:
        self.heater_on = False
        self.ac_on = False

    def perceive_and_act(self, temperature: int) -> str:
        """Update internal state and return actions for one temperature reading."""
        actions = []

        if temperature < 20 and not self.heater_on:
            self.heater_on = True
            actions.append("Heater ON")
        elif temperature >= 20 and self.heater_on:
            self.heater_on = False
            actions.append("Heater OFF")

        if temperature > 26 and not self.ac_on:
            self.ac_on = True
            actions.append("AC ON")
        elif temperature <= 26 and self.ac_on:
            self.ac_on = False
            actions.append("AC OFF")

        if not actions:
            actions.append("No change")
        return f"Temperature: {temperature}°C -> {', '.join(actions)}"


def main() -> None:
    temperatures = [18, 22, 25, 25, 19]
    agent = TemperatureAgent()
    print("Model-based reflex agent trace:")
    for temperature in temperatures:
        print(agent.perceive_and_act(temperature))


if __name__ == "__main__":
    main()
