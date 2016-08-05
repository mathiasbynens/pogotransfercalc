# pogotransfercalc [![Build status](https://travis-ci.org/mathiasbynens/pogotransfercalc.svg?branch=master)](https://travis-ci.org/mathiasbynens/pogotransfercalc) [![PyPI version](https://img.shields.io/pypi/v/pogotransfercalc.svg)](https://pypi.python.org/pypi/pogotransfercalc)

_pogotransfercalc_ makes it easy to calculate how many Pokémon you should transfer before kicking off an evolution spree in Pokémon GO. Like [PidgeyCalc.com](http://www.pidgeycalc.com/), but in Python instead of through a web-based UI.

## Installation

Using [pip](https://pip.pypa.io/):

```sh
$ pip install terminaltables
```

## Usage

```py
from pogotransfercalc import calculate

result = calculate(pokemon_count=40, candy_count=288, evolution_cost=12)
print result
# → {'evolutions': 27, 'transfers': 10}
result = calculate(pokemon_count=40, candy_count=288, evolution_cost=12, transfer_after_evolving=True)
print result
# → {'evolutions': 29, 'transfers': 4}
```

## Credits

Thanks to Bai Chan Kheo for creating [PidgeyCalc.com](http://www.pidgeycalc.com/)! This package is essentially a programmatic version of Bai’s tool.

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

_pogotransfercalc_ is available under the [MIT](https://mths.be/mit) license.
