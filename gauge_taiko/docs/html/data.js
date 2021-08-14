var tags = ["input", "output", "boundary", "partial-input", "invalid", "error", "smoke", "decimals", "decimal", "division", "integration", "addition", "exponential", "subtraction", "validation", "integer"]
var specs = [{"path":"specs\\functional\\addition.html","name":"Addition","scenarios":[{"name":"Addition between integers","tags":["integer","smoke","addition"]},{"name":"Addition between decimals","tags":["decimals","smoke","addition"]},{"name":"Addition between integers and decimals","tags":["integer","decimal","addition"]},{"name":"Addition result in exponential form","tags":["exponential","boundary","addition"]},{"name":"Number can be added to itself","tags":["partial-input","addition"]}]},{"path":"specs\\functional\\division.html","name":"Division","scenarios":[{"name":"Division between integers","tags":["integer","smoke","division"]},{"name":"Division between decimals","tags":["decimals","smoke","division"]},{"name":"Division between integers and decimals","tags":["integer","decimal","division"]},{"name":"Division result in exponential form","tags":["exponential","boundary","division"]},{"name":"Number can be divided by itself","tags":["partial-input","division"]},{"name":"Divide by zero","tags":["invalid","error","division"]}]},{"path":"specs\\functional\\subtraction.html","name":"Subtraction","scenarios":[{"name":"Subtraction between integers","tags":["integer","smoke","subtraction"]},{"name":"Subtraction between decimals","tags":["decimals","smoke","subtraction"]},{"name":"Subtraction between integers and decimals","tags":["integer","decimal","subtraction"]},{"name":"Subtraction result in exponential form","tags":["exponential","boundary","subtraction"]},{"name":"Number can be subtracted from itself","tags":["partial-input","subtraction"]}]},{"path":"specs\\integration\\integration.html","name":"Operator Integration","scenarios":[{"name":"Addition \u0026 Subtraction","tags":["addition","subtraction","integration"]},{"name":"Subtraction \u0026 Division","tags":["subtraction","division","integration"]},{"name":"Addition \u0026 Division","tags":["addition","division","integration"]}]},{"path":"specs\\validation\\validation.html","name":"Input \u0026 Output Validation","scenarios":[{"name":"Initial Input","tags":["input","validation"]},{"name":"Default Decimal Input","tags":["input","partial-input","validation"]},{"name":"Maximum input length","tags":["input","validation"]},{"name":"Multiple zeros input not allowed","tags":["input","validation"]},{"name":"Leading zero input not allowed","tags":["input","validation"]},{"name":"Large number output is displayed in exponential form","tags":["output","validation"]},{"name":"Decimal output is displayed up to 8 decimal digits","tags":["output","validation"]}]}]