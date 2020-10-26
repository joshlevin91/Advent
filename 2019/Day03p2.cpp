#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <array>
#include <boost/algorithm/string.hpp>
#include <boost/functional/hash.hpp>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(){

	ifstream inputFile("Day03.txt");
	string line;
	vector<string> firstPath;
	vector<string> secondPath;
	unordered_map<array<int, 2>, int, boost::hash<array<int, 2>>> firstWire;
	unordered_map<array<int, 2>, int, boost::hash<array<int, 2>>> secondWire;
	set<int> stepsToIntersections;


	getline(inputFile, line);
	boost::split(firstPath, line, [](char c){return c == ',';});

	getline(inputFile, line);
	boost::split(secondPath, line, [](char c){return c == ',';});

	array<int, 2> loc {0, 0};
	int totalSteps = 0;
	for (auto move : firstPath){
		char dir = move[0];
		int steps = stoi(move.substr(1));
		if (dir == 'R'){
			for (int i = 1; i <= steps; i++){
				loc[0]++;
				firstWire.insert({loc, ++totalSteps});
			}
		}
		else if (dir == 'L'){
			for (int i = 1; i <= steps; i++){
				loc[0]--;
				firstWire.insert({loc, ++totalSteps});
			}
		}
		else if (dir == 'U'){
			for (int i = 1; i <= steps; i++){
				loc[1]++;
				firstWire.insert({loc, ++totalSteps});
			}
		}
		else {
			for (int i = 1; i <= steps; i++){
				loc[1]--;
				firstWire.insert({loc, ++totalSteps});
			}
		}
	}

	loc[0] = 0;
	loc[1] = 0;
	totalSteps = 0;
	for (auto move : secondPath){
		char dir = move[0];
		int steps = stoi(move.substr(1));
		if (dir == 'R'){
			for (int i = 1; i <= steps; i++){
				loc[0]++;
				secondWire.insert({loc, ++totalSteps});
			}
		}
		else if (dir == 'L'){
			for (int i = 1; i <= steps; i++){
				loc[0]--;
				secondWire.insert({loc, ++totalSteps});
			}
		}
		else if (dir == 'U'){
			for (int i = 1; i <= steps; i++){
				loc[1]++;
				secondWire.insert({loc, ++totalSteps});
			}
		}
		else {
			for (int i = 1; i <= steps; i++){
				loc[1]--;
				secondWire.insert({loc, ++totalSteps});
			}
		}
	}

	for (auto it_f = firstWire.begin(); it_f != firstWire.end(); it_f++){
		auto it_s = secondWire.find(it_f->first);
		if (it_s != secondWire.end()){
			stepsToIntersections.insert(it_f->second + it_s->second);
		}
	}

	cout << *stepsToIntersections.begin() << endl;
}