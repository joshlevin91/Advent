#include <fstream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <iostream>

using namespace std;

void printInts(const vector<int>& ints){
	for (auto i : ints){
		cout << i << ", ";
	}
	cout << endl;
}

int main(){

	ifstream inputFile("Day02.txt");
	string line;
	vector<string> tokens;
	vector<int> og_ints;
	int target = 19690720;
	bool done = false;

	// Parse string
	getline(inputFile, line);
	boost::split(tokens, line, boost::is_any_of(","));

	// Convert to integers
	for (auto token : tokens){
		og_ints.push_back(stoi(token));
	}

	for (int n = 0; n <= 99; n ++){
		for (int v = 0; v <= 99; v++){

			vector<int> ints(og_ints.begin(), og_ints.end());

			// Inputs
			ints[1] = n;
			ints[2] = v;

			for (int i = 0; i < ints.size(); i += 4){

				// Opcode 99: terminate
				if (ints[i] == 99){
					break;
				}

				// Opcode 1: add
				else if (ints[i] == 1){
					ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]];
				}

				// Opcode 2: multiply
				else {
					ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]];
				}
			}

			if (ints[0] == target){
				cout << 100*n + v << endl;
				done = true;
				break;
			}
		}
		if (done) break;
	}
}