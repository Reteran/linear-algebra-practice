#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
	
	if(orders == NULL)
		printf("Not able to open orders.csv");
	else
	{
		char buffer[1000];
		char *token;
		
		fgets(buffer, 1000, orders);
		token = strtok(buffer, ",");
		
		int c = 1;
		while(token != NULL)
		{
			if(c==1)
				eqns = atoi(token);
			if(c==2)
				unns = atoi(token);
			token = strtok(NULL, ",");
			c++;
		}
	}
	
	long double x[unns];
	for (int i = 0; i < unns; i++)
	{
		x[i] = 0;
	}

	//printf("eqns=%d unns=%d\n", eqns, unns);      for debugging purposes
	long double aug_matrix[eqns][unns + 1];

	if (f_aug == NULL)
		printf("Not able to open aug_matrix");
	else
	{
		char buffer[1000];
		char *token;
		int i = 0;
		while (fgets(buffer, 1000, f_aug))
		{
			token = strtok(buffer, ",");
			int j = 0;
			while (token != NULL)
			{
				aug_matrix[i][j] = strtold(token, NULL);
				token = strtok(NULL, ",");
				j++;
			}
			i++;
		}
	}

	// for debugging purposes
	/*for (int i = 0; i < eqns; i++)
	{
		for (int j = 0; j < unns + 1; j++)
		{
			printf("%.18Lf ", aug_matrix[i][j]);   // was: %f
		}
		printf("\n");
	}*/

	fclose(orders);
	fclose(f_coeff);
	fclose(f_aug);

	FILE *solution;
	solution = fopen("Data/solution.csv", "w");
	for (int i = 0; i < 20; i++)
	{
		for (int p = 0; p < eqns; p++)
		{
			long double sum_non_diag = 0;
			for (int q = 0; q < unns; q++)
			{
				if (q != p)
				{
					sum_non_diag += x[q] * aug_matrix[p][q];
				}
			}
			x[p] = (1.0L / aug_matrix[p][p]) * (aug_matrix[p][unns] - sum_non_diag); 
		}

		for (int i = 0; i < unns; i++)
		{
			if (i == unns - 1)
				fprintf(solution, "%.18Lf\n", x[i]);   
			else
				fprintf(solution, "%.18Lf,", x[i]);  
		}
	}
	fclose(solution);
}