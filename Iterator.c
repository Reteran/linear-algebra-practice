#include <stdio.h>
#include <string.h>

int main()
{
	int eqns, unns;
	
	FILE *orders;
	orders = fopen("Data/orders.csv", "r");
	FILE *f_coeff;
	f_coeff = fopen("Data/coeff_matrix.csv", "r");
	FILE *f_aug;
	f_aug = fopen("Data/aug_matrix.csv", "r");
	if(f_coeff == NULL)
		printf("Not able to open coeff_matrix");
	if(f_aug == NULL)
		printf("Not able to open aug_matrix");
	if(orders == NULL)
		printf("Not able to open orders.csv");
	
	char row[100];
	fgets(row, 100, orders);
	char *matorders;
	
	matorders = strtok(row, ",");
	
	int length = sizeof(row)/sizeof(row[0]);
	for(int i = 0; i < length; i++)
		printf("%c ", row[i]);
	
	fclose(orders);
	fclose(f_coeff);
	fclose(f_aug);
}