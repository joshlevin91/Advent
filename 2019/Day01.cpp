#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){

	ifstream inputFile ("Day01.txt");
	string line;

	int sum = 0;
	while(getline(inputFile, line)){

		int mass = stoi(line);

		do {
			int fuel = mass / 3 - 2;
			mass = max(fuel, 0);
			sum += mass;
		} while (mass > 0);
	}

	cout << sum << endl;
}