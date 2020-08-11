#include <iostream>
#include <fstream>
#include <array>
#include <string>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

void setCorners(array<int, 4>& corners, string line, int len);
vector<string> parseString(string s);

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

		// Follow turn on instructions
		if (line.rfind("turn on", 0) == 0){

			setCorners(corners, line, 8);

			for (int i = corners[0]; i <= corners[2]; i++){
				for (int j = corners[1]; j <= corners[3]; j++){
					lights[i][j]++;
				}
			}
		}

		// Follow turn off instructions
		else if (line.rfind("turn off", 0) == 0){

			setCorners(corners, line, 9);

			for (int i = corners[0]; i <= corners[2]; i++){
				for (int j = corners[1]; j <= corners[3]; j++){
					if (lights[i][j] > 0){
						lights[i][j]--;
					}
				}
			}
		}

		// Follow toggle instructions
		else if(line.rfind("toggle", 0) == 0){

			setCorners(corners, line, 7);

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

// Set corners listed in instructions
void setCorners(array<int, 4>& corners, string line, int len){

	line = line.substr(len);
	vector<string> tokens = parseString(line);

	corners[0] = stoi(tokens[0]);
	corners[1] = stoi(tokens[1]);
	corners[2] = stoi(tokens[3]);
	corners[3] = stoi(tokens[4]);
}

// Parse string and return tokens delimited by a comma or space
vector<string> parseString(string s){

	regex delims("[, ]");
	sregex_token_iterator first{s.begin(), s.end(), delims, -1}, last;
	vector<string> tokens{first, last};

	return tokens;
}