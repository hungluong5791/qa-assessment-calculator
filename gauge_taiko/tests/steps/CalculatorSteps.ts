import { expect, util } from "chai";
import { Gauge, Step, Table } from "gauge-ts";
import Calculator from "../pages/Calculator";
import * as utils from "../utils/utils";


export default class CalculatorSteps {
    @Step('Input the formula <formula>')
    public async inputFormula(formula: string) {
        const parsedFormula = utils.parseFormula(formula);
        Gauge.writeMessage(`Formula input: ${parsedFormula}`);

        await Calculator.inputFormula(parsedFormula);
    }

    @Step('Perform the calculation')
    public async calculate() {
        await Calculator.calculate();
    }

    @Step([
        'The Calculator result should be <output>',
        'The Calculator should display <output>',
    ])
    public async checkOutput(expectedOutput: string) {
        const calculatorResult = await Calculator.getResult();
        Gauge.writeMessage(`Calculator output: ${calculatorResult}`);

        expect(calculatorResult).to.equal(expectedOutput);
    }
}