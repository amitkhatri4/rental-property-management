#include <stdio.h>
#include <stdlib.h>

#define MAX_MONTHS 12

void readData(float data[], int *count);
int findMaxMonth(float data[], int count);
int findMinMonth(float data[], int count);
float findTotal(float data[], int count);
float findAverage(float data[], int count);
void sortData(float data[], float sorted[], int count);
float findMedian(float sorted[], int count);
void displayResults(float data[], int count);

int main() {
    float rainfall[MAX_MONTHS];
    int count = 0;

    readData(rainfall, &count);
    displayResults(rainfall, count);

    return 0;
}

void readData(float data[], int *count) {
    FILE *file = fopen("rainfall.txt", "r");
    if (file == NULL) {
        printf("Error: Could not open rainfall.txt\n");
        exit(1);
    }

    while (*count < MAX_MONTHS && fscanf(file, "%f", &data[*count]) == 1) {
        (*count)++;
    }

    fclose(file);
}

int findMaxMonth(float data[], int count) {
    int maxIndex = 0;
    for (int i = 1; i < count; i++) {
        if (data[i] > data[maxIndex]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

int findMinMonth(float data[], int count) {
    int minIndex = 0;
    for (int i = 1; i < count; i++) {
        if (data[i] < data[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

float findTotal(float data[], int count) {
    float total = 0;
    for (int i = 0; i < count; i++) {
        total += data[i];
    }
    return total;
}

float findAverage(float data[], int count) {
    return findTotal(data, count) / count;
}

void sortData(float data[], float sorted[], int count) {
    for (int i = 0; i < count; i++) {
        sorted[i] = data[i];
    }

    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (sorted[j] > sorted[j + 1]) {
                float temp = sorted[j];
                sorted[j] = sorted[j + 1];
                sorted[j + 1] = temp;
            }
        }
    }
}

float findMedian(float sorted[], int count) {
    if (count % 2 == 0) {
        return (sorted[count/2 - 1] + sorted[count/2]) / 2;
    } else {
        return sorted[count/2];
    }
}

void displayResults(float data[], int count) {
    int maxMonth = findMaxMonth(data, count);
    int minMonth = findMinMonth(data, count);
    float total = findTotal(data, count);
    float average = findAverage(data, count);
    float sorted[MAX_MONTHS];
    sortData(data, sorted, count);
    float median = findMedian(sorted, count);

    printf("Highest Rainfall Month: %d (%.2f inches)\n", maxMonth + 1, data[maxMonth]);
    printf("Lowest Rainfall Month: %d (%.2f inches)\n", minMonth + 1, data[minMonth]);
    printf("Total Rainfall: %.2f inches\n", total);
    printf("Average Rainfall: %.2f inches\n", average);
    printf("Median Rainfall: %.2f inches\n", median);
    printf("Sorted Rainfall Data:\n");
    for (int i = 0; i < count; i++) {
        printf("%.2f ", sorted[i]);
    }
    printf("\n");
}
