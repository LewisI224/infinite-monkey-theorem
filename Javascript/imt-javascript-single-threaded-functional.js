var attemptNo = 0;
var bestAttempt = 0;
var bestAttemptNo = 0;
var alphabet = 'abcdefghijklmnopqrstuvwxyz ';
var text = 'hello';
var textIndex = 0;

function type(monkeyName) {
    var noMistakes = true;
    while(noMistakes) {
        pickedLetter = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
        if(pickedLetter == text.toLowerCase()[textIndex]) {
            textIndex ++;
            if (textIndex == text.length) {
                console.log("Full text has been typed");
                console.log("Monkeys name is " + monkeyName);
                console.log("On attempt number " + attemptNo);
                process.exit(1)
            }
        }
        else {
            if (textIndex > bestAttempt) {
                bestAttempt = textIndex;
                bestAttemptNo = attemptNo;
            }  
            noMistakes = false;
        }
            
    }

}

while(true) {
    
    attemptNo ++;
    textIndex = 0;
    type("Quincy");
    console.log("Best Attempt " + bestAttempt + " on attempt number " + bestAttemptNo);
}
