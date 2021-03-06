#!/usr/bin/env python
# coding=utf-8

from unittest import TestCase

from pogotransfercalc import calculate

class TestCalculation(TestCase):

	def test_scenario_1(self):
		result = calculate(pokemon_count=20, candy_count=144, evolution_cost=12)
		self.assertEqual(result['transfers'], 0)
		self.assertEqual(result['evolutions'], 13)

	def test_scenario_2(self):
		result = calculate(pokemon_count=40, candy_count=288, evolution_cost=12)
		self.assertEqual(result['transfers'], 10)
		self.assertEqual(result['evolutions'], 27)

	def test_scenario_3(self):
		result = calculate(
			pokemon_count=40,
			candy_count=288,
			evolution_cost=12,
			transfer_after_evolving=True)
		self.assertEqual(result['transfers'], 4)
		self.assertEqual(result['evolutions'], 29)

	def test_scenario_4(self):
		result = calculate(pokemon_count=10, candy_count=6, evolution_cost=12)
		self.assertEqual(result['transfers'], 6)
		self.assertEqual(result['evolutions'], 1)

	def test_scenario_5(self):
		result = calculate(pokemon_count=11, candy_count=390, pokedex_number=129)
		self.assertEqual(result['transfers'], 10)
		self.assertEqual(result['evolutions'], 1)

	def test_scenario_6(self):
		result = calculate(pokemon_count=2, candy_count=11, pokedex_number=10)
		self.assertEqual(result['transfers'], 1)
		self.assertEqual(result['evolutions'], 1)

	def test_scenario_7(self):
		result = calculate(pokemon_count=2, candy_count=999, pokedex_number=3)
		self.assertEqual(result['transfers'], 0)
		self.assertEqual(result['evolutions'], 0)
