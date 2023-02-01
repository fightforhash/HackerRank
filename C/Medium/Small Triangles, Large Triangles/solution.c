#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

double area(triangle* tr){
    double p = (tr->a + tr->b + tr ->c) / 2.0;
    return sqrt(p * (p - tr->a) * (p - tr->b) * (p - tr->c));     
}


int compare (triangle* tr1, triangle* tr2){
    double a1 = area(tr1);
    double a2 = area(tr2);
    if (a1 > a2){
        return 1;
    }
    if (a1 < a2){
        return 0;
    }else{
        return 0;
    }
    
}



void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    int i,  j;
    triangle element;
    for (int i = 1; i< n; i++){
        element = tr[i]; 
        j = i-1; 
        
        while (j >=0 && compare(&tr[j], &element) > 0){
            tr[j+1] = tr[j];
            j = j-1;
        }
        tr[j+1] = element;
    }
    
}
int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
