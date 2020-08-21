#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h> 

using namespace std;

int main(){

	int numNiceStrings = 0;
	ifstream inputFile ("input.txt");

	string stringToCheck;

	while(getline(inputFile, stringToCheck)){

		// Contains a pair of any two letters that appear at least twice in the string without overlapping
		bool pair = false;
		for (int i = 0; i < stringToCheck.length()-1; i++){
			for (int j = 0; j < stringToCheck.length()-1; j++){
				if (abs(i-j) > 1 && stringToCheck[i] == stringToCheck[j] && stringToCheck[i+1] == stringToCheck[j+1]){
					pair = true;
					break;
				}
			}
		}

		if(!pair){
			continue;
		}

		// Contains at least one letter which repeats with exactly one letter between them
		bool repeat = false; 
		for (int i = 0; i < stringToCheck.length()-2; i++){
			if(stringToCheck[i] == stringToCheck[i+2]){
				repeat = true;
				break;
			}
		}
		
		if (!repeat){
			continue;
		}

		numNiceStrings++;

	}

	cout << "Number of nice strings: " << numNiceStrings << endl;

	return 0;
}