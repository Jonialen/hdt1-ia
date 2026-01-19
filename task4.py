# task4.py (task4.py)

from random import choice, randint

class Enviroment:
    def __init__(self):
        self.temperature = randint(0, 35)
        self.accions = {"enfriar": 0 - randint(1, 3), 
                        "calentar": randint(1, 3),
                        "esperar": choice([-1, 0, 1])}

    def get_percept(self):
        return self.temperature

    def update(self, action):
        self.temperature += self.accions[action]

class Agent:
    def act(self, perception):
        if perception > 30:
            return "enfriar"
        elif perception < 15:
            return "calentar"
        else:
            return "esperar"

def main():
    env = Enviroment()
    agent = Agent()

    for step in range(1, 11):
        current_temp = env.get_percept()
        action = agent.act(current_temp)
        env.update(action)
        new_temp = env.get_percept()

        print(f"Iteracion {step}")
        print(f"Temperatura actual: {current_temp}°C")
        print(f"Accion del agente: {action}")
        print(f"Nueva temperatura: {new_temp}°C\n")

main()

