print("### REQUEST TACTICAL DOLL ###")

nama_tactical_doll = input("masukan nama tactical doll: ")
firepower = int(input("masukan jumlah firepower: "))
rate_of_power = int(input("masukan jumlah rate of power: "))
accuracy = int(input("masukan jumlah accuracy: "))
evasion = int(input("masukan jumlah evasion: "))

damage_per_second = (firepower*rate_of_power)/60
combat_effectiveness = (30*firepower)+(40*(rate_of_power**2/120))+(15*(accuracy+evasion))
print("\n")
print("### SUCCESS ###")
print(f"Tactical Doll:  {nama_tactical_doll}")
print(f"Firepower: {firepower}")
print(f"Rate Of Power: {rate_of_power}")
print(f"Accuracy: {accuracy}")
print(f"Evasion: {evasion}")
print(f"Damage per second: {damage_per_second}")
print(f"Combat Effectiveness: {combat_effectiveness}")
