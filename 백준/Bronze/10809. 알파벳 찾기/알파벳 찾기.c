#include <stdio.h>

int main(void) {
	char s1[101] = { NULL };

	int cnt[26];

	scanf("%s", s1);


	for (int i = 0; i < 26; i++)  //cnt 배열 -1로 초기화
		cnt[i] = -1;

	for (int i = 'a'; i<='z'; i++) {
		for (int j = 0; j<100; j++)
		{

			if (s1[j] == i) {
				cnt[i - 97] = j;
				break;

			}
		}
	}


	for (int i = 0; i < 26; i++) {
		printf("%d ", cnt[i]);
	}
	printf("\n");



	return 0; 
}

