# Subtraction
The Calculator should correctly perform subtraction operation

tags: subtraction

* Open Calculator Fullscreen application

## Subtraction between integers
The Calculator should correctly perform addition between integers, including zero and negative numbers

tags: integer, smoke

   |formula         |result|
   |----------------|------|
   |1 - 1           |0     |
   |2 - 3           |-1    |
   |110457 - 3101   |107356|
   |10 - 4 - 0      |6     |
   |(-1) - 1 - (-10)|8     |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Subtraction between decimals
The Calculator should correctly perform addition between decimals, including negative numbers

tags: decimals, smoke

   |formula                       |result|
   |------------------------------|------|
   |0.21 - 0.2                    |0.01  |
   |1.123 - 3.019                 |-1.896|
   |5.135 - (-0.98)               |6.115 |
   |0.72 - (-0.31) - 0.4 - (-0.12)|0.75  |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Subtraction between integers and decimals
The Calculator should correctly perform addition between integers and decimals, including zero and negative numbers

tags: integer, decimal

   |formula                           |result|
   |----------------------------------|------|
   |0.34 - 9                          |-8.66 |
   |97 - 7.0                          |90    |
   |2 - (-1.2) - 3 - 0                |0.2   |
   |(-6) - (-8.5) - (-3.14) - 4 - (-2)|3.64  |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Subtraction result in exponential form
The Calculator should show Subtraction result in exponential form when the result is larger than the maximum display range
i.e 1 000 000 000 and up

tags: exponential, boundary

   |formula                 |result|
   |------------------------|------|
   |(-1) - 999999999        |-1e+9 |
   |(-999999999) - 999999999|-2e+9 |
   |1 - (-999999999)        |1e+9  |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Number can be subtracted from itself
Partial Subtraction input should result in the operand being subtracted from itself

tags: partial-input

   |formula       |result|
   |--------------|------|
   |1 -           |0     |
   |(-3) -        |0     |
   |(-999999999) -|0     |
* Calculate the formula <formula>
* The Calculator result should be <result>
