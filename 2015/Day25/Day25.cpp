#include <iostream>
#include <cmath>

long int CodeAtLoc(const int row, const int column, long int code = 20151125, int n = 2);

int main(){

	std::cout << CodeAtLoc(3010, 3019) << std::endl;
}

long int CodeAtLoc(const int row, const int column, long int code, int n){
	
	int i = n + 1;
	int j = 0;

	while (i > 1) {
		i--;
		j++;
		code = code*252533 % 33554393;
		if (i == row & j == column){
			break;
		}
	}

	if (i == row & j == column){
		return code;
	}
	else {
		return CodeAtLoc(row, column, code, n + 1);
	}

}