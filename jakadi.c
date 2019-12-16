#include<stdio.h>

/*
Attend un pointeur sur un array de caractères (une chaîne en C) 
et l'affiche.
*/
void dit_papa(char * p)
{
    printf("%s\n", p);
}
 
 
/*
Attend deux entiers et les multiple
*/
int multiplier(long a, long b)
{
    return a * b;
}
 
/*
Attend un pointeur de pointeur sur un array de char
parce qu'on aime les risques.
*/
void jakadi(char ** p)
{
    printf("%s\n", *p);
}

int main()
{
	return multiplier(1, 1);
}