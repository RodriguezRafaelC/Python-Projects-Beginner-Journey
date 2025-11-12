import random

your_Pokemons = ["Charmander", "Acie", "Kent"]
acie_Skills = ["Sucking Dih", "Licking Dih", "Blowing Job", "Spread Cheeks"]
rattata_Skills = ["Tackle", "Tail Whip"]
rattata_useSkills = random.choices(rattata_Skills)

print("A wild Rattata appeard!")
print("Choose your Pokemon")
for i in your_Pokemons:
    print("-", i)

choose_Pokemon = input("\nPick : ").lower()

if choose_Pokemon == "acie":
    print("Acie Skills")
    for i in acie_Skills:
        print("-", i)
    
    use_Skills = input("Acie use- : ").lower()

    if use_Skills == "sucking dih":
        print("Acie use Sucking Dih!")
        print("Acie sucked Rattata's Dih")
        print(f"Rattata used {rattata_useSkills}")