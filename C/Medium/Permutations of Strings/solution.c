#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void swap(char** s1, char** s2){
    char* temp = *s1; 
    *s1 = *s2;
    *s2 = temp;
    
}
int next_permutation(int n, char **s)
{
	/**
	* Complete this method
	* Return 0 when there is no next permutation and 1 otherwise
	* Modify array s to its next permutation
	*/
    int k, i, l;
    printf("%d",k);
    k = i = l = 0;
    
    for (i = n-2; i >= 0; i--){
        if(strcmp(s[i], s[i+1]) < 0){
            k = i;
            break;
        }
        
    }
    if (i== -1){
        return 0;
    
    }for(i = n-1; i>= k+1; i--)
        if ((strcmp(s[k],s[i])) < 0){
            l = i;
            break;
        }
        
        
    swap(&s[k], &s[l]);    
    
     
        
     int inner = k + 1 + n - 1;
     int cond = inner / 2;
     for (i = n-1; i> cond; i--)
         swap(&s[i], &s[inner-i]);
     
        
    return 1;
    
}
int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}