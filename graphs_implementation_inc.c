#include<stdio.h>
#include<string.h>
void main(){//void
	char vote[5];
	int numbe_of_verteces;
	printf("enter the number of vertecs:");
	scanf("%d",&numbe_of_verteces);
	int matrix[numbe_of_verteces ][numbe_of_verteces];
	for(int i=0; i<numbe_of_verteces; i++){
		for(int j=0; j<numbe_of_verteces; j++){
			printf("is %d and %d are connected: ",i,j);
			printf("y or n:");
			scanf("%s",vote);
			//printf("%s",vote);
		if(strcmp(vote,"y")==0){
			matrix[i][j] =1;
		}
		else{matrix[i][j] = 0;}
		}
	}
	for(int i=0; i<numbe_of_verteces; i++){
		for(int j=0; j<numbe_of_verteces; j++){
			printf("%d",matrix[i][j]);
		}
		printf("\n");
	}


}//void
