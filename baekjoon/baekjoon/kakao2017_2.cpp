#include <iostream>
#include <math.h>

using namespace std;

int cal(char* str) {
	int i, tmp;
	if (str[1] == 0) {	//점수 : 10
		tmp = 10;
		for (i = 2; str[i] != '\0'; i++) {
			if (str[i] == 'S')
				tmp = (int)pow(tmp, 1);
			else if (str[i] == 'D')
				tmp = (int)pow(tmp, 2);
			else if (str[i] == 'T')
				tmp = (int)pow(tmp, 3);
			else if (str[i] == '*')
				tmp *= 2;
			else if (str[i] == '#')
				tmp *= -1;
		}
	}
	else if (str[1] != 0) {	//점수 : 10점 미만
		tmp = str[0] - '0';
		for (i = 1; str[i] != '\0'; i++) {
			if (str[i] == 'S')
				tmp = (int)pow(tmp, 1);
			else if (str[i] == 'D')
				tmp = (int)pow(tmp, 2);
			else if (str[i] == 'T')
				tmp = (int)pow(tmp, 3);
			else if (str[i] == '*')
				tmp *= 2;
			else if (str[i] == '#')
				tmp *= -1;
		}
	}

	return tmp;
}

int main() {
	while(1) {
		int i = 0, k = 0, l = 0, temp = 0, result[10] = { 0, }, ee = 0;
		char input[100], tempStr[100] = "\0";
		cin >> input;
		while (1) {
			if (i > 0) {
				if (('0' <= input[i] && input[i] <= '9') || input[i] == '\0') {
					for (int j = temp; j < i; j++) {
						if (input[j] == '*')
							result[l - 1] *= 2;
					
						tempStr[k++] = input[j];
					}
					temp = i;
					result[l++] = cal(tempStr);

					for (int j = 0; j <= k; j++)
						tempStr[j] = '\0';
					k = 0;
				}
			}
			if (input[i] == '\0')
				break;
			i++;
		}
		for (int j = 0; j < 10; j++)
			ee += result[j];
		cout << "result : " << ee << endl;

	}
	return 0;
}

/*
2. 피보나치 수열

int fibo(int a) {
	if (a == 0)
		return 0;
	if (a == 1)
		return 1;
	if (a > 1) {
		return fibo(a - 1) + fibo(a - 2);
	}
}

int main() {
	int i, j;
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 5; j++)
			printf("%d\t", fibo(5*i+j));
		printf("\n");
	}

	return 0;
}
*/
/*
1. 문자열 역출력

void reverseString(char *s1, char *s2) {
	int i = 0, j = 0, length = 0;
	while (s1[i] != '\0')
		i++;
	
	length = i;
	for (i = length - 1; i >= 0; i--)
		s2[j++] = s1[i];
	
	s2[j] = '\0';
}

int main() {
	char str[100];
	char reverse_str[100];
	cout << "input string : ";
	cin.getline(str, 100, '\n');
	reverseString(str, reverse_str);
	cout << "reverse string : " << reverse_str << endl;
	return 0;
}
*/