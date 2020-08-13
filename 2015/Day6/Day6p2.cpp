#include <iostream>
#include <fstream>
#include <array>
#include <string>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

string setCorners(array<int, 4>& corners, string line);

int main(){

	// Create and initialize 2D array of lights (all off)
	const int arrLen = 1000;
	array<array<int, arrLen>, arrLen> lights;

	for (int i = 0; i < arrLen; i++){
		for (int j = 0; j < arrLen; j++){
			lights[i][j] = 0;
		}
	}


	string line;
	fstream inputFile ("input.txt");

	while(getline(inputFile, line)){

		array<int, 4> corners;
		string instructions = setCorners(corners, line);

		// Follow turn on instructions
		if (instructions == "turn on"){
			for (int i = corners[0]; i <= corners[2]; i++){
				for (int j = corners[1]; j <= corners[3]; j++){
					lights[i][j]++;
				}
			}
		}

		// Follow turn off instructions
		else if (instructions == "turn off"){
			for (int i = corners[0]; i <= corners[2]; i++){
				for (int j = corners[1]; j <= corners[3]; j++){
					if (lights[i][j] > 0){
						lights[i][j]--;
					}
				}
			}
		}

		// Follow toggle instructions
		else if(instructions == "toggle"){
			for (int i = corners[0]; i <= corners[2]; i++){
				for (int j = corners[1]; j <= corners[3]; j++){
					lights[i][j] += 2;
				}
			}
		}
	}

	// Calculate total brightness
	int totalBrightness = 0;
	
	for (int i = 0; i < arrLen; i++){
		for (int j = 0; j < arrLen; j++){
			totalBrightness += lights[i][j];
		}
	}

	cout << totalBrightness << endl;
}

// Set corners and return instructions
string setCorners(array<int, 4>& corners, string line){

	size_t pos = line.find_first_of("123456789");

	string instructions = line.substr(0, pos-1);
	string restOfLine = line.substr(pos);

	regex delims("[, ]");
	sregex_token_iterator first{restOfLine.begin(), restOfLine.end(), delims, -1}, last;
	vector<string> tokens{first, last};

	corners[0] = stoi(tokens[0]);
	corners[1] = stoi(tokens[1]);
	corners[2] = stoi(tokens[3]);
	corners[3] = stoi(tokens[4]);

	return instructions;
}