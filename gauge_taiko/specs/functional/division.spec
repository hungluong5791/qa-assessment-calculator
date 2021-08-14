# Division
The Calculator should correctly perform division operation

tags: division

* Open Calculator Fullscreen application

## Division between integers
The Calculator should correctly perform division between integers, including zero and negative numbers

tags: integer, smoke

   |formula        |result     |
   |---------------|-----------|
   |3 / 1          |3          |
   |0 / 3          |0          |
   |999 / 3 / 3    |111        |
   |(-2) / 4       |-0.5       |
   |2 / (-3)       |-0.66666667|
   |(-1000)/(-5000)|0.2        |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Division between decimals
The Calculator should correctly perform division between decimals, including negative numbers

tags: decimals, smoke

   |formula            |result    |
   |-------------------|----------|
   |0.22 / 0.11        |2         |
   |10.0 / 1.25        |8         |
   |(-0.8) / 4.2 / 24.4|-0.0078064|
   |0.4 / (-0.2)       |-2        |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Division between integers and decimals
The Calculator should correctly perform division between integers and decimals, including zero and negative numbers

tags: integer, decimal

   |formula                |result     |
   |-----------------------|-----------|
   |100.2 / 2              |50.1       |
   |(-1) / 2.5 / (-1000)   |0.0004     |
   |10000 / 0.98 / (-7) / 1|-1457.72595|
* Calculate the formula <formula>
* The Calculator result should be <result>

## Division result in exponential form
The Calculator should show Division result in exponential form when the result is larger than the maximum display range
i.e 1 000 000 000 and up

tags: exponential, boundary

   |formula           |result  |
   |------------------|--------|
   |999999999 / 0.1   |10e+9   |
   |1 / 999999999     |1e-9    |
   |(-999) / 999999999|-9.99e-7|
* Calculate the formula <formula>
* The Calculator result should be <result>

## Number can be divided by itself
Partial Division input should result in the operand being divided to itself

tags: partial-input

   |formula|result|
   |-------|------|
   |5 /    |1     |
   |(-1) / |1     |
   |3.14 / |1     |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Divide by zero
Division by zero should result in an error

tags: invalid, error

   |formula  |result|
   |---------|------|
   |1 / 0    |Error |
   |-1000 / 0|Error |
   |3.14 / 0 |Error |
* Calculate the formula <formula>
* The Calculator result should be <result>
