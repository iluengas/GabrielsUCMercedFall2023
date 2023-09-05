let lastInputNum = 0;
let currentInputNum = 0;
let totalToDisp=0;
let currInpStr='';
let lastReadCommand = '';
let currCommand = '';

function addOperation(){

    console.log("ADD OPERATION EXECUTED");

    currCommand = '+';

    currentInputNum=parseFloat(currInpStr);

    equalOperation(currCommand);

}

function equalOperation(currCommand) {
    console.log("EQUAL OPERATION EXECUTED");
    console.log("CURRENT INP: " + currentInputNum);
    console.log("LAST INP: " + lastInputNum);
    console.log("LAST COMMAND: " + lastReadCommand);
    console.log("CURR COMMAND: " + currCommand)



    switch(currCommand) {
        case "+":
            totalToDisp = currentInputNum + lastInputNum;
            document.getElementById("calcDisplay").innerHTML = totalToDisp;
            lastInputNum = currentInputNum;
            currInpStr = '';
            lastReadCommand = currCommand;
            break;
        case "-":
            currentInputNum = currentInputNum - lastInputNum;
            break;
        case "x":
            currentInputNum = currentInputNum * lastInputNum;
            break;
        case "/":
            currentInputNum = currentInputNum/lastInputNum;
            break;
        case "=":
            // currentInputNum = currentInputNum + lastInputNum;
            //currentInputNum=parseFloat(currInpStr);
            if (lastReadCommand != "="){
                currCommand = lastReadCommand;
                equalOperation(currCommand);

            }
            break;
    }
    currentInputNum = 0;
}

function clearDisp() {

    console.log("DISPLAY CLEAR OPERATION EXECUTED")
    lastInputNum = 0;
    currentInputNum = 0;
    currInpStr = '';

    document.getElementById("calcDisplay").innerHTML = '';

}

function append(inp){
    currInpStr += inp;

    document.getElementById("calcDisplay").innerHTML = currInpStr;

    currentInputNum=parseFloat(currInpStr);
}