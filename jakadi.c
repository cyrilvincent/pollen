#include <stdio.h>

/*
Attend un pointeur sur un array de caractères (une chaîne en C) 
et l'affiche.
*/
__declspec(dllexport) void dit_papa(char * p)
{
    printf("%s\n", p);
}
 
 
/*
Attend deux entiers et les multiple
*/
__declspec(dllexport) int multiplier(long a, long b)
{
    return a * b;
}
 
/*
Attend un pointeur de pointeur sur un array de char
parce qu'on aime les risques.
*/
__declspec(dllexport) void jakadi(char ** p)
{
    printf("%s\n", *p);
}

__declspec(dllexport) int main()
{
	return multiplier(1, 1);
}