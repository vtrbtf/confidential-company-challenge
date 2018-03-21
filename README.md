# Backend Challenge

## Problem
Given cargos and trucks, find the optimal mapping to reduce distance, considering that is not possible to reuse trucks.

## Solution
Matrix of geographical coordinates differences between of package pickup and truck location, combined with permutation of of cargo ordering based on index.

### Complexity
___Suboptimal___, considering that it's using all available permutations for `range(len(cargos))` making the overall complexity `O(len(cargos)!)`.
The solution was based on a brute-force implementation and could be improved if I had more time

## Usage

> Python 3.6.4  
> Linux Mint 18.3

`$ python3.6 main.py`

### Data
All the `csv` files are under `data` directory.

### Output
Each product has it's own section, with details about the selected truck and route and a generated link to google maps

### Docker
In order to isolate environments, it's also possible to use Docker. Its already available a Dockerfile that could be used to run the solution:  
`$ docker build -t loadsmart-python . && docker run loadsmart-python`

## Tests
`$ python3.6 -m unittest discover tests/ -p '*_test.py'`


