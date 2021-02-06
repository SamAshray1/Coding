#include <iostream>
using namespace std;
/* Will return the count of all the possible arrangements 
of length N that can be derived from the characters 
of an input string of length N.*/

long int Factorial(int n);

int main(){
	int n;
	long int nfac;
	cin >> n;
	nfac=Factorial(n);
	char ar[n];
	for(int i=0;i<n;i++)
	cin >> ar[i];
	int i=0, alphabet[26]={0},j;
	
	//Finding the frequency of each alphabet in given string
	while (ar[i] != '\0') {
      if (ar[i] >= 'A' && ar[i] <= 'Z') {
         j = ar[i] - 'A';
         ++alphabet[j];
      }
      ++i;
   }
	for(int i=0;i<n;i++)
	if(alphabet[i]>1)
	nfac=nfac/Factorial(alphabet[i]);
	
	cout << nfac;
	
	
}

long int Factorial(int n){
	int fac=1;
	for(int i=2;i<=n;i++)
	fac=fac*i;
	return fac;
};
