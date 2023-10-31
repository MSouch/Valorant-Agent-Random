import random

names = ["Phoenix", "Raze", "Jett", "Yoru", "Neon", "Reyna", "Sage", "Cypher", "Chamber", "Killjoy", "Omen", "Viper", "Brimstone", "Astra", "Harbor", "Sova", "Breach", "Skye", "KAY/O", "Fade", "Deadlock", "iso"]

name_agent_dict = {}

for n in range(5):
    name = input("Enter your name to get a random Valorant agent: ")
    chosen_name = random.choice(names)
    name_agent_dict[name] = chosen_name
    print(f"{name}, your random agent is {chosen_name}")
    
    if n == 4:
        break

for name, agent in name_agent_dict.items():
    print("---------------------------------------")
    print(f"{name}, your random agent was {agent}")
    print("---------------------------------------")