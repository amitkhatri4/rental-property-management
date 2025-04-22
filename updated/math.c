#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function Prototypes
void printMenu();
void displayProblem(int choice, int num1, int num2);
int readAnswer();
void displayResult(int correctAnswer, int userAnswer);

int main() {
    int choice, num1, num2, userAnswer, correctAnswer;
    
    srand(time(0)); // Seed for random number generation
    
    while (1) {
        printMenu();
        scanf("%d", &choice);
        
        if (choice < 1 || choice > 3) {
            printf("Invalid choice. Exiting program.\n");
            break;
        }
        
        num1 = rand() % 100;
        num2 = rand() % 100;
        
        displayProblem(choice, num1, num2);
        
        userAnswer = readAnswer();
        
        switch (choice) {
            case 1:
                correctAnswer = num1 + num2; 
                break;
            case 2:
                correctAnswer = num1 - num2;
                break;
            case 3:
                correctAnswer = num1 * num2;
                break;
        }
        
        displayResult(correctAnswer, userAnswer);
    }
    return 0;
}

// Function to display menu
void printMenu() {
    printf("\nMath Tutor Program\n");
    printf("1. Add\n");
    printf("2. Subtract\n");
    printf("3. Multiply\n");
    printf("Enter your choice (1-3): ");
}

// Function to display the problem
void displayProblem(int choice, int num1, int num2) {
    char operator;
    switch (choice) {
        case 1: operator = '+'; break;
        case 2: operator = '-'; break;
        case 3: operator = '*'; break;
    }
    printf("\n  %d\n %c %d\n -----\n", num1, operator, num2);
}

// Function to read the user’s answer
int readAnswer() {
    int answer;
    printf("Your answer: ");
    scanf("%d", &answer);
    return answer;
}

// Function to display the result
void displayResult(int correctAnswer, int userAnswer) {
    if (userAnswer == correctAnswer) {
        printf("Congratulations! Your answer is correct.\n");
    } else {
        printf("Incorrect. The correct answer is %d.\n", correctAnswer);
    }
}
