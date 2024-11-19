#!/usr/bin/env python3
"""
TP 1, p 33
"""


"""
ion en python est très importante.
Création de Pokémon & interaction avec un 
utilisateur– Etape 1
 Aspect du cours à utiliser lors du TP:
 - Variables- Input- Structures de données
 - Fonctions
 - Créer des Pokémon en utilisant des variables pour stocker leurs caractéristiques 
(nom/type/HP/attaque/défense)
- Stocker la liste des Pokémon dans une structure de données
- Créer une interaction avec l'utilisateur pour créer deux Pokémon
"""

# Création de Pokémon

def iteration():
    print("Création de Pokémon")
    print("Combien de fois voulez-vous itérer la fonction pokemon_creation?")
    iteration = int(input())
    print("Nombre d'itérations: ", iteration)
    pokemons = []
    for i in range(iteration):
        # Placer le return dans une liste pour stocker les pokemons
        pokemons.append(pokemon_creation())
    print("Liste des Pokémon créés:")
    print(pokemons)

def pokemon_creation():
    nom_pokemon = input("Nom du Pokémon: ")
    type_pokemon = input("Type du Pokémon: ")
    hp_pokemon = int(input("HP du Pokémon: "))
    attaque_pokemon = int(input("Attaque du Pokémon: "))
    defense_pokemon = int(input("Défense du Pokémon: "))

    # Stockage des caractéristiques des Pokémon dans un dictionnaire
    pokemon = {
        "nom": nom_pokemon,
        "type": type_pokemon,
        "hp": hp_pokemon,
        "attaque": attaque_pokemon,
        "defense": defense_pokemon
    }
    # Affichage des Pokémon créés
    #print("Pokémon:")
    #print(pokemon)
    return pokemon

iteration()