HATFD1035
Print Pascal's Triangle
Write a program to generate and print the first n rows of Pascal’s triangle
without using built-in math or array functions. For n = 5, the output
should be:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Solution:
//Print pascal's triangle
#include <stdio.h>
void generatePascalsTriangle(int n) {
for (int i = 0; i < n; i++) {
int number = 1; // Start with 1 at the beginning of each row
for (int k = 0; k < n - i - 1; k++) {
printf(" ");
}
for (int j = 0; j <= i; j++) {
printf("%d ", number);
number = number * (i - j) / (j + 1); // Compute the next element
}
printf("\n"); // Move to the next row
}
}
int main() {
int n = 5; // Set the number of rows for Pascal's triangle
generatePascalsTriangle(n);
return 0;
}
