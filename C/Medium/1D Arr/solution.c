#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int size; 
    int result = 0;
    scanf("%d", &size);
    
    for (int i = 0; i < size; i++){
    int *arr = (int*)malloc(size * sizeof(int));

      scanf("%d", &arr[i]);  
      result += arr[i];
      
    }
    printf("%d\n", result);
    return 0;
}
