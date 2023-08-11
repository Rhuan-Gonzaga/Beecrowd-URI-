#include <iostream>
 
using namespace std;
 
int main() {
 
    /**
     * Escreva a sua solução aqui
     * Code your solution here
     * Escriba su solución aquí
     */
     
     float salario;
   
   scanf("%f",&salario);
   
   
   if (salario <= 400) {
       int porcento = 15;
       printf("Novo salario: %.2f\n", (salario + (salario * 15)/100));
       printf("Reajuste ganho: %.2f\n",salario * 15/100);
       printf("Em percentual: %d %%\n",porcento);
   }

   else if (salario > 400 and salario <= 800) {
       int porcento = 12;
       printf("Novo salario: %.2f\n", (salario + (salario * 12)/100));
       printf("Reajuste ganho: %.2f\n",salario * 12/100);
       printf("Em percentual: %d %%\n",porcento);
   }
   
   
   else if (salario > 800 and salario <= 1200) {
        int porcento = 10;
       printf("Novo salario: %.2f\n", (salario + (salario * 10)/100));
       printf("Reajuste ganho: %.2f\n",salario * 10/100);
       printf("Em percentual: %d %%\n",porcento);
   }
   
    else if (salario > 1200 and salario <= 2000) {
        int porcento = 7;
       printf("Novo salario: %.2f\n", (salario + (salario * 7)/100));
       printf("Reajuste ganho: %.2f\n",salario * 7/100);
       printf("Em percentual: %d %%\n",porcento);
   }
   
   else{
       int porcento = 4;
       printf("Novo salario: %.2f\n", (salario + (salario * 4)/100));
       printf("Reajuste ganho: %.2f\n",salario * 4/100);
       printf("Em percentual: %d %%\n",porcento);
   }
   
     
     
     
}