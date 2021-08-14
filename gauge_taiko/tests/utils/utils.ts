import { Keypad } from "../enums/Keypad";

export const SUPPORTED_OPERATORS = ['+', '-', '*', '/'];

export const VALID_FORMULA_REGEX = /[0-9()+\-*/\.]/;

export const parseFormula = (formulaStr: string): string[] => {
    const formula = formulaStr.split('');
    const sanitizedFormula = sanitize(formula);
    const parsedFormula = parseBracketedNumbers(sanitizedFormula);

    return parsedFormula;
}

export const isOperator = (input: string): boolean => {
    return SUPPORTED_OPERATORS.includes(input);
}

export const isOperand = (input: string): boolean => {
    return !isOperator(input);
}

function sanitize(formula: string[]): string[] {
    return formula.filter(element => VALID_FORMULA_REGEX.test(element));
}

function parseBracketedNumbers(formula: string[]): string[] {
    let parsedFormula = [];

    let inBrackets = false;
    let bracketedChars = [];

    formula.forEach(element => {
        if (!isBracket(element) && !inBrackets) {
            parsedFormula.push(element);
            return;
        }

        if (isBracket(element)) {
            if (isOpeningBracket(element)) {
                inBrackets = true;
                return;
            }

            if (isClosingBracket(element)) {
                // Should input the sign button after the number
                if (bracketedChars[0] === '-') {
                    bracketedChars.splice(0, 1);
                    bracketedChars.push(Keypad.POSITIVE_NEGATIVE);
                }
                parsedFormula = parsedFormula.concat(bracketedChars);

                inBrackets = false;
                bracketedChars = [];
                return;
            }
        }

        if (!isBracket(element) && inBrackets) {
            bracketedChars.push(element);
            return;
        }
    });

    return parsedFormula;
}

function isBracket(input: string): boolean {
    return isOpeningBracket(input) || isClosingBracket(input);
}

function isOpeningBracket(input: string): boolean {
    return input === '(';
}

function isClosingBracket(input: string): boolean {
    return input === ')';
}
