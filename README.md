# py-core
Pounce lang aimed at running on microPython or circuitPython. The code is just for experimentation with Joy-lang concatenative code on a microprocessor.

py-core is not made for speed, but has the advantage that it fits inside a python micro-controller ecosystem (micropython, circuitpyton) with lots of hardware specific libraries for interfacing with sensors, actuators, portable to a growing variety of microprocessor and dev boards. Otherwise see pounce-lang/c-core for an interpreter that is a little closer to the metal (maybe the c-core can be built as a python module. That would combine the faster c-core for use in the portable python environments).

## tests
python3 parser_tests.py

python3 runtime_tests.py