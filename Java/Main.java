import java.util.Random;

public class Main {

    static int attemptNo = 0;
    static int bestAttempt = 0;
    static int bestAttemptNo = 0;
    static String alphabet = "abcdefghijklmnopqrstuvwxyz ";
    static String text = "hello";
    
    static int textIndex = 0;
    static Random random = new Random();
    public static void main(String[] args) {
        text = text.toLowerCase();
        while(true) {
            attemptNo ++;
            textIndex = 0;
            type("Quincy");
            System.out.print("Best Attempt " + bestAttempt + " on attempt number " + bestAttemptNo);
        }

    }

    static void type(String monkeyName) {
        boolean noMistakes = true;
        while(noMistakes) {
            char pickedLetter = alphabet.charAt(random.nextInt(alphabet.length()));
            if(pickedLetter == text.charAt(textIndex)) {
                textIndex ++;
                if (textIndex == text.length()) {
                    System.out.println("Full text has been typed.");
                    System.out.println("Monkeys name is " + monkeyName);
                    System.out.println("On attempt number " + attemptNo);
                    System.exit(0);
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
}




