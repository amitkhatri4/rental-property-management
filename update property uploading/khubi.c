#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100

// Function prototypes
int readData(FILE *fp, int *model, int *type, float *cost, int *quantity);
float calculateValue(float cost, int quantity);
void printLine(FILE *out, int model, const char *typeName, float cost, int quantity, float value);
const char* getTypeName(int type);

int main() {
    FILE *inFile, *outFile;
    int model, type, quantity;
    float cost, value;

    float totalRoad = 0, totalMountain = 0, totalHybrid = 0;
    float grandTotal = 0;

    inFile = fopen("bikes.txt", "r");
    if (inFile == NULL) {
        printf("Error opening bikes.txt\n");
        return 1;
    }

    outFile = fopen("report.txt", "w");
    if (outFile == NULL) {
        printf("Error creating report.txt\n");
        return 1;
    }

    fprintf(outFile, "%-10s %-10s %-10s %-10s %-10s\n", "Model", "Type", "Cost", "Quantity", "Value");
    fprintf(outFile, "-----------------------------------------------------------\n");

    while (readData(inFile, &model, &type, &cost, &quantity)) {
        value = calculateValue(cost, quantity);
        const char *typeName = getTypeName(type);
        printLine(outFile, model, typeName, cost, quantity, value);

        if (type == 1) totalRoad += value;
        else if (type == 2) totalMountain += value;
        else if (type == 3) totalHybrid += value;

        grandTotal += value;
    }

    fprintf(outFile, "\nTotal Value by Type:\n");
    fprintf(outFile, "Road: $%.2f\n", totalRoad);
    fprintf(outFile, "Mountain: $%.2f\n", totalMountain);
    fprintf(outFile, "Hybrid: $%.2f\n", totalHybrid);
    fprintf(outFile, "-------------------\n");
    fprintf(outFile, "Grand Total: $%.2f\n", grandTotal);

    fclose(inFile);
    fclose(outFile);

    printf("Report written to report.txt\n");

    return 0;
}

// Reads one line of bike data
int readData(FILE *fp, int *model, int *type, float *cost, int *quantity) {
    return fscanf(fp, "%d %d %f %d", model, type, cost, quantity) == 4;
}

// Calculates the total value for a bike type
float calculateValue(float cost, int quantity) {
    return cost * quantity;
}

// Prints one formatted line to the report file
void printLine(FILE *out, int model, const char *typeName, float cost, int quantity, float value) {
    fprintf(out, "%-10d %-10s $%-9.2f %-10d $%-9.2f\n", model, typeName, cost, quantity, value);
}

// Converts type code to string
const char* getTypeName(int type) {
    switch (type) {
        case 1: return "Road";
        case 2: return "Mountain";
        case 3: return "Hybrid";
        default: return "Unknown";
    }
}
