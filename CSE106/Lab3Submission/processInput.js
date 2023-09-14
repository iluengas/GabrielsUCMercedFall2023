let lastInputNum = 0;
let lastReadCommand = '';
let displayStr='';
let heldVar = 0;

            
function disableDecBtn() {
    document.getElementById("decimalBtn").disabled = true;
}

function enableDecBtn() {
    document.getElementById("decimalBtn").disabled = false;
}

function clearDisp() {
    console.log("DISPLAY CLEAR OPERATION EcurrentInputNumECUTED")
    lastInputNum = 0;
    displayStr = '';
    lastReadCommand = '';
    document.getElementById("calcDisplay").innerHTML = '0';
}

function addOperation(currentInputNum, lastInputNum) {
    displayValue = lastInputNum + currentInputNum;
    return displayValue;
}

function subtractOperation(currentInputNum, lastInputNum) {
    displayValue = lastInputNum - currentInputNum;
    return displayValue;
}

function multiplicationOperation(currentInputNum, lastInputNum) {
    displayValue = lastInputNum * currentInputNum;
    return displayValue;
}

function divisionOperation(currentInputNum, lastInputNum) {
    displayValue = lastInputNum / currentInputNum;
    return displayValue;
}

function performCalculation(inputCommand, currentInputNum) {
    console.log("BEGIN CALCULATION");
    let displayValue = 0;

    switch (inputCommand) {
        case "+":
            displayValue = addOperation(currentInputNum, lastInputNum);
            document.getElementById("calcDisplay").innerHTML = displayValue;
            lastInputNum = displayValue;
            displayStr = '';
            lastReadCommand = inputCommand;
            break;
        case "-":
            if (lastReadCommand == "") {
                displayValue = subtractOperation(currentInputNum*-1, lastInputNum);
            } else {
                displayValue = subtractOperation(currentInputNum, lastInputNum);
            }
            document.getElementById("calcDisplay").innerHTML = displayValue;
            lastInputNum = displayValue;
            displayStr = '';
            lastReadCommand = inputCommand;
            break;
        case "*":
            if (lastReadCommand == "") {
                displayValue = multiplicationOperation(currentInputNum, 1);
            } else   {
                displayValue = multiplicationOperation(currentInputNum, lastInputNum);
            } 
            document.getElementById("calcDisplay").innerHTML = displayValue;
            lastInputNum = displayValue;
            displayStr = '';
            lastReadCommand = inputCommand;
            break;
        case "/":
            if (lastReadCommand == "") {
                lastInputNum = currentInputNum;
                displayStr = '';
                lastReadCommand = inputCommand;
                break;
            } else {
                displayValue = divisionOperation(currentInputNum, lastInputNum);
                document.getElementById("calcDisplay").innerHTML = displayValue;
                lastInputNum = displayValue;
                displayStr = '';
                lastReadCommand = inputCommand;
                break; 
            }
       
        case "=":
            performCalculation(lastReadCommand, heldVar);
            break;
        default:
            console.log("UNKOWN INPUT");
            break;
    }

    console.log("CURRENT INP: " + currentInputNum);
    console.log("LAST INP: " + lastInputNum);
    console.log("CURR COMMAND: " + inputCommand);
    console.log("LAST COMMAND: " + lastReadCommand);
    console.log("HeldVar" + heldVar)
}

function calcInput(inp){

    currentInputNum = parseFloat(displayStr);

    switch (inp) {
        case "+":
            if (isNaN(currentInputNum)){
                performCalculation(inp, 0);
            } else {
                heldVar = currentInputNum;
                performCalculation(inp, currentInputNum);
            }
            break;
        case "-":
            if (displayStr == ""){
                displayStr = "-";
                document.getElementById("calcDisplay").innerHTML = displayStr;
                break;
            } else {
                if (isNaN(currentInputNum)){
                    performCalculation(inp, 0);
                } else {
                    heldVar = currentInputNum;
                    performCalculation(inp, currentInputNum);
                }
                break;                
            }
        case "*":
            if (isNaN(currentInputNum)){
                performCalculation(inp, 1);
            } else {
                heldVar = currentInputNum;
                performCalculation(inp, currentInputNum);
            }
            break;
        case "/":
            if (isNaN(currentInputNum)){
                performCalculation(inp, 1);
            } else {
                heldVar = currentInputNum;
                performCalculation(inp, currentInputNum);
            }
            break;
        case "=":
            if (isNaN(currentInputNum)){             
                performCalculation(inp, 0);
                break;
            } else {
                heldVar = currentInputNum;
                performCalculation(inp, currentInputNum);
                break;
            }
        default:
            displayStr += inp;
            document.getElementById("calcDisplay").innerHTML = displayStr;
            break;
    }
}