
let heldEntry = false;

var operation = '';
var currNum, prevNum = 0;;
var lastOperation = '';

var count = 0;

var temp;

function append(strInp) {
    let x = document.getElementById("calcDisplay");

    if (heldEntry) {
        x.textContent = '';
        heldEntry = false;
    } 

    if (x.textContent == '0') {
        x.textContent = strInp;
    } else {
        x.textContent += strInp;
    }
}

function clearDisp(){
    lastInputNum = 0;
    lastCommand = '';
    document.getElementById("calcDisplay").textContent = 0;
    pendCommand = '';
    enableDecBtn();
}

function disableDecBtn() {
    document.getElementById("decimalBtn").disabled = true;
}

function enableDecBtn() {
    document.getElementById("decimalBtn").disabled = false;
}

function changeSign() {
    calcDisplayString = document.getElementById("calcDisplay").textContent;

    if (calcDisplayString.charAt(0) == "-") {
        slicedString = calcDisplayString.slice(1);
        document.getElementById("calcDisplay").textContent = slicedString;
    } else if (calcDisplayString.charAt(0) == "0") {
        document.getElementById("calcDisplay").textContent = "-";
    } 
    else {
        calcDisplayString = "-" + calcDisplayString;
        document.getElementById("calcDisplay").textContent = calcDisplayString;
    }
}

function holdEntry(enteredBool) {
    let x = document.getElementById("calcDisplay");
    if (enteredBool) {
        heldEntry = true;
    } else {
        heldEntry = false;
    }
}

function runCalc(){
 
    let computation;
    var prev = prevNum;

    var curr = parseFloat(document.getElementById("calcDisplay").textContent);

    if ((operation == '') && (lastOperation != ""))  {
        operation = lastOperation;
    }

    console.log("Operation: " + operation);
    console.log("CurrNum: " + currNum);
    console.log("PrevNum: " + prevNum);
    console.log("Curr: " + curr);
    console.log();

    switch(operation) {
        case "+":
            if (count > 0) {
                computation = prev + temp;
            } else {
                computation = prev + curr;
            }
            
            break;
        default:
            console.log("ERROR-Unkown operation passed to runCalc")
            break;
    }
    document.getElementById("calcDisplay").textContent = computation;

    prevNum = curr;
  
    lastOperation = operation;
    operation = '';

    console.log("Operation: " + operation);
    console.log("CurrNum: " + currNum);
    console.log("PrevNum: " + prevNum);
    console.log("Curr: " + curr);
    console.log();
}
function chooseCommand(command) {
    if (operation !== command){
        operation = command;
        count = 0;
    }

    if (operation === command || command == "=") {
        if (command == "=") {
            count += 1;
            if (count < 1) {
                var temp = parseFloat(document.getElementById("calcDisplay").textContent);
                runCalc(temp)
            }
        }
        runCalc(parseFloat(document.getElementById("calcDisplay").textContent));
    }
    // prevNum = parseFloat(document.getElementById('calcDisplay').textContent);
    // currNum = 0;
}