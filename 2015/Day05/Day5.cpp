#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

bool stringContains(string mainString, string subString);

int main(){

	int numNiceStrings = 0;
	ifstream inputFile ("input.txt");

	string stringToCheck;

	while(getline(inputFile, stringToCheck)){

		// Contains at least three vowels
		string const vowels("aeiouAEIOU");
		int vowelCount = count_if(stringToCheck.begin(), stringToCheck.end(), 
			[&](char c){ return vowels.end() != find(vowels.begin(), vowels.end(), c); });

		if (vowelCount < 3){
			continue;
		}

		// Contains at least one letter that appears twice in a row
		bool twiceInRow = false; 
		for (int i = 0; i < stringToCheck.length()-1; i++){
			if(stringToCheck[i] == stringToCheck[i+1]){
				twiceInRow = true;
				break;
			}
		}

		if (!twiceInRow){
			continue;
		}

		// Does not contain strings: ab, cd, pq, or xy
		if (stringContains(stringToCheck, "ab") || stringContains(stringToCheck, "cd") || 
			stringContains(stringToCheck, "pq") || stringContains(stringToCheck, "xy")){
			continue;
		}

		numNiceStrings++;

	}

	cout << "Number of nice strings: " << numNiceStrings << endl;

	return 0;
}


bool stringContains(string mainString, string subString){
	if (mainString.find(subString) != string::npos){
		return true;
	}
	else {
		return false;
	}
}