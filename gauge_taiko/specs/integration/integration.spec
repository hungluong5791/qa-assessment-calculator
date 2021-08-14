# Operator Integration
The Calculator should be able to perform calculation using multiple operators

tags: integration

* Open Calculator Fullscreen application

## Addition & Subtraction
The Calculator should be able to perform calculation with both addition and subtraction
Both these operator should be equal in priority
The order of operation should not affect the result

tags: addition, subtraction

   |formula                 |result|
   |------------------------|------|
   |1 + 9 - 5               |5     |
   |1 - 5 + 9               |5     |
   |(-1000) + 500 - 7 + 0   |-507  |
   |(-2.0) - 3.14 + 8.2 - 10|-6.94 |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Subtraction & Division
The Calculator should be able to perform calculation with both subtraction and division
Division should have higher priority than subtraction

tags: subtraction, division

   |formula        |result|
   |---------------|------|
   |100000 - 8 / 4 |99998 |
   |20 / 5 - 7     |-3    |
   |11.04 / 0.5 - 3|19.08 |
   |5 - 0 / 5      |5     |
   |5 / 0 + 1      |Error |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Addition & Division
The Calculator should be able to perform calculation with both addition and division
Division should have higher priority than addition

tags: addition, division

   |formula                   |result|
   |--------------------------|------|
   |999999999 + 20 / 10       |1e+9  |
   |(-1) / 4 + 2.5            |2.25  |
   |9 + 7 / 1 + (-1000) / 2000|15.5  |
* Calculate the formula <formula>
* The Calculator result should be <result>
