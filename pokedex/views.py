from django.shortcuts import render

def index(request):
    pokemons = ["Charizar", "pikachu", "Metagross", "tyranitar", "gengar"]
    return render(request, 'index.html', {"pokemons": pokemons})

def pokemon_details(request, pokemon):
    return render(request, 'details.html', {"pokemon": pokemon})
