#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
	int N,M;
	scanf("%d", &N);
	int arr[N];
	int i,j;
	
	for(int i = 0; i < N; i++) {
		int x;
		scanf("%d",&x);
		if(i == 0)
			arr[i] = x;
		else
			arr[i] = x + arr[i-1];
	}
	
	scanf("%d", &M);
	
	while(M) {
		
		scanf("%d %d", &i, &j);
		if(i == 1)
			printf("%d\n",arr[j-1]);
		else
			printf("%d\n",arr[j-1] - arr[i-2]); 
		M--;		
	}
	return 0;
}