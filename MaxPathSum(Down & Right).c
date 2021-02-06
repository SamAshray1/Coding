#include <stdio.h>
#include <limits.h>

int MaxArray(int ar[],int n){
	int max=INT_MIN;
	for(int i=0;i<n*n;i++)
	{	if(ar[i]>max)
		max=ar[i];}
	return max;
}

void MaxPathSumRD(int n,int ar[][n], int i, int j,int sum,int arr[]){
	if(i<n && j<n){
	sum = sum + ar[i][j];
	MaxPathSumRD(n,ar,i,j+1,sum,arr);
	MaxPathSumRD(n,ar,i+1,j,sum,arr);
	if(i==n-1 && j==n-1){
	for(int i=0;i<n*n;i++)
	if(arr[i]==0){
	arr[i]=sum;
	break;}
	}
}
}

void main(){
	int n,max,count=0;
	scanf("%d",&n);
	int ar[n][n];
	int arr[n*n];
	for(int i=0;i<n*n;i++)
	arr[i]=0;
	for(int i=0;i<n;i++)
	for(int j=0;j<n;j++)
	scanf("%d",&ar[i][j]);
	MaxPathSumRD(n,ar,0,0,0,arr);
	max = MaxArray(arr,n);
	for(int i=0;i<n*n;i++)
	{	if(arr[i]==max)
		count++;}	
printf("%d %d",max,count);

}
