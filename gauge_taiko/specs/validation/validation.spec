# Input & Output Validation
The Calculator should have correct input & output behaviours

tags: validation

* Open Calculator Fullscreen application

## Initial Input
The Calculator should display correct initial input

tags: input

* The Calculator should display "0"

## Default Decimal Input
The Calculator should correctly parse partial decimal input i.e .5 as 0.5

tags: input, partial-input

   |formula |result|
   |--------|------|
   |.5 + 1  |1.5   |
   |3 + .25 |3.25  |
   |.25 + .4|0.65  |
* Calculate the formula <formula>
* The Calculator result should be <result>

## Maximum input length
The Calculator should allow a maximum input length of 9 digits
Negative sign (-) and decimal point (.) is not counted

tags: input

   |formula      |result    |
   |-------------|----------|
   |999999999    |999999999 |
   |(-999999999) |-999999999|
   |9999999999999|999999999 |
   |0.12345678   |0.12345678|
   |0.123456789  |0.12345678|
* Input the formula <formula>
* The Calculator should display <result>

## Multiple zeros input not allowed
The Calculator should not allow input consist of only zeroes

tags: input

   |formula  |result|
   |---------|------|
   |00       |0     |
   |000000000|0     |
* Input the formula <formula>
* The Calculator should display <result>

## Leading zero input not allowed
The Calculator should not allow input with leading zero(s)

tags: input

   |formula|result|
   |-------|------|
   |012    |12     |
   |01.32  |1.32  |
* Input the formula <formula>
* The Calculator should display <result>

## Large number output is displayed in exponential form
When displaying result that is between +/- 1000000000 (one billion) - exclusive - the result should be display in full
Results outside that range should be displayed in exponential form

tags: output

   |formula      |result   |
   |-------------|---------|
   |999999998 + 1|999999999|
   |999999999 + 1|1e+9     |
* Calculate the formula <formula>
* The Calculator should display <result>

## Decimal output is displayed up to 8 decimal digits
When displaying decimal result, the result can have up to 8 decimal digits

tags: output

   |formula|result    |
   |-------|----------|
   |1 / 2  |0.5       |
   |2 / 3  |0.66666667|
* Calculate the formula <formula>
* The Calculator result should be <result>
