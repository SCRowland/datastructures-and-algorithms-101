# datastructures-and-algorithms-101

Toy examples to learn / revise algorithms. For personal consumption only.

This repo does not contain production code, the wheel will be re-invented in aid of learning and refreshing techniques.


## Testing

Most tests include benchmarking to compare implementations.

#### Run all tests and benchmarks:

`pipenv run pytest`

#### Run only benchmarks (skip unit tests):

`pipenv run pytest --benchmark-only`

### Run only unit tests (skip benchmarks):

`pipenv run pytest --benchmark-skip`

#### Run specific test group:

`pipenv run pytest algorithms/dynamic_programming`
