#!/usr/bin/env python
# coding=utf-8

from .cost import cost

def calculate(
	pokemon_count=0, candy_count=0,
	pokedex_number=0, evolution_cost=12,
	transfer_after_evolving=False):

	candies_gained_on_evolution = 1
	if transfer_after_evolving:
		candies_gained_on_evolution = 2

	if pokedex_number:
		if pokedex_number in cost:
			evolution_cost = cost[pokedex_number]
		else:
			return {
				'transfers': 0,
				'evolutions': 0
			}

	evolution_count = 0
	transfer_count = 0

	# Handle the initial evolutions, without accounting for later transfers of
	# evolved Pokémon.
	while True:
		# Break when there aren’t enough Pokémon or candies.
		if candy_count // evolution_cost == 0 or pokemon_count == 0:
			break
		else:
			# Evolve a Pokémon.
			pokemon_count -= 1
			candy_count -= evolution_cost
			candy_count += candies_gained_on_evolution
			evolution_count += 1
			# Break if out of Pokémon.
			if pokemon_count == 0:
				break

	# Handle the remaining evolutions, made possible by transferring the
	# freshly-evolved Pokémon.
	while True:
		# Break when there aren’t enough Pokémon or candies.
		if (candy_count + pokemon_count) < (evolution_cost + 1) or pokemon_count == 0:
			break

		# Keep transferring until there are enough candies for another evolution.
		while candy_count < evolution_cost:
			transfer_count += 1
			pokemon_count -= 1
			candy_count += 1

		# Evolve a Pokémon.
		pokemon_count -= 1
		candy_count -= evolution_cost
		candy_count += candies_gained_on_evolution
		evolution_count += 1

	return {
		'transfers': transfer_count,
		'evolutions': evolution_count
	}
