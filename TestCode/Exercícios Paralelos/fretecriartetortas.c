#include <stdio.h>
#include <locale.h>

//Este programa calcula o valor do frete para entrega de tortas.

int main(){
	
	setlocale(LC_ALL, "Portuguese");
	
	float frete, Km, torta, preco, carro, gasolina, tx;
	
	printf("------------------------------");
	printf("\n\tCRIARTE TORTAS\n");
	printf("------------------------------");

	printf("\n\n- Insira o valor da torta: ");
	scanf("%f", &torta);
	
	printf("- Insira quantos quilômetros é de casa até o cliente: ");
	scanf("%f", &Km);
	
	//Valores em real
	carro = 10;		//Quilometragem por litro de gasolina.
	gasolina = 5;	//Valor do litro da gasolina.
	tx = 5;			//Valor da taxa de entrega.
	
	frete = (((Km * 2)/carro) * gasolina) + tx;		//Cálculo do frete. "Km * 2" é referente a entrega e retorno do carro.
	preco = frete + torta;							//Preço final para o cliente.
	
	printf("\n------------------------------");

	printf("\nTorta: R$%.2f", torta);
	printf("\nFrete: R$%.2f", frete);
	printf("\nPREÇO FINAL: R$%.2f", preco);


	getch();
	
	return 0;
}
