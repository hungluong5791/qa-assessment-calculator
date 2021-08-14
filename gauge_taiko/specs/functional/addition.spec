# Addition
The Calculator should correctly perform addition operation

tags: addition

* Open Calculator Fullscreen application

## Addition between integers
The Calculator should correctly perform addition between integers, including zero and negative numbers

tags: integer, smoke

   |formula              |result|
   |---------------------|------|
   |1+1                  |2     |
   |2 + 3                |5     |
   |1 + 10 + 100         |111   |
   |999 + 10             |1009  |
   |(-5) + 99 + 1 + (-10)|85    |
   |1 + 0 + (-3)         |-2     |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Addition between decimals
The Calculator should correctly perform addition between decimals, including negative numbers

tags: decimals, smoke

   |formula             |result|
   |--------------------|------|
   |0.11 + 0.2          |0.31  |
   |0.2 + 0.9           |1.1   |
   |0.135 + 0.98        |1.115 |
   |0.72 + 0.4 + (-0.12)|1     |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Addition between integers and decimals
The Calculator should correctly perform addition between integers and decimals, including zero and negative numbers

tags: integer, decimal

   |formula                         |result  |
   |--------------------------------|--------|
   |0.11 + 2                        |2.11    |
   |92 + 0.9                        |92.9    |
   |10000 + 0.98 + 3 + 0            |10003.98|
   |1 + (-0.5) + (-3.14) + 3 + (-10)|-9.64   |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Addition result in exponential form
The Calculator should show Addition result in exponential form when the result is larger than the maximum display range
i.e 1 000 000 000 and up

tags: exponential, boundary

   |formula              |result|
   |---------------------|------|
   |999999999 + 1        |1e+9  |
   |999999999 + 999999999|2e+9  |
   |(-1) + (-999999999)  |-1e+9 |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Number can be added to itself
Partial Addition input should result in the operand being added to itself

tags: partial-input

   |formula    |result|
   |-----------|------|
   |1 +        |2     |
   |-1 +       |-2    |
   |999999999 +|2e+9  |
* Calculate the formula <formula>
* The Calculator result should be <result>
