import { click, evaluate, press, waitFor } from "taiko";
import { Keypad } from "../enums/Keypad";
import * as utils from "../utils/utils";

class Calculator {

    async inputFormula(formula: string[]) {
        for (let element of formula) {
            // separate operand and operator input for possible extension regarding operands
            if (utils.isOperand(element)) {
                await this.inputOperand(element);
                continue;
            }

            if (utils.isOperator(element)) {
                await this.inputOperator(element);
                continue;
            }
        }
    }

    async inputOperand(operand: string) {
        const operandDigits = operand.split('');
        for (let digit of operandDigits) {
            await press(digit);
            await waitFor(100);
        }
        // await press(operandDigits);
    }

    async inputOperator(operator: string) {
        await press(operator);
    }

    async calculate() {
        await press(Keypad.EQUAL);
    }

    async getResult(): Promise<string> {
        const calculatorText: string = await evaluate(() => document.querySelector('#fullframe')['contentWindow']['exportRoot']['showscreen_txt']['text']);

        // clean up the result text (may contain spaces)
        return calculatorText.replace(/\s/g, '');
    }
}

export default new Calculator();