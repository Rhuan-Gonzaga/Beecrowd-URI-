#include <stdio.h>
#include <stdlib.h>

/*A seguinte sequ�ncia de n�meros 0 1 1 2 3 5 8 13 21... � conhecida como s�rie de Fibonacci. 
Nessa sequ�ncia, cada n�mero, depois dos 2 primeiros, � igual � soma dos 2 anteriores. 
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros n�meros dessa s�rie.*/

main(){
	
 int x,y, a=0,b=1,c=0;
    scanf("%d", &x);
    
    for(y=1; y<x; y++)
    {
        if(y%2==1)
        {
            printf("%d ",c);
            c=a+b;
            a=c;
        }
        else if(y==2)
            printf("%d ",c);
        else if(y%2==0)
        {
            printf("%d ",c);
            c=a+b;
            b=c;
        }
    }
    printf("%d\n",c);
    return 0;

		
	
}
