#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <set>
#include <array>
#include <boost/algorithm/string.hpp>
#include <boost/functional/hash.hpp>
#include <iostream>
#include <cstdlib>

using namespace std;

int manhattanDistance(const array<int, 2>& pos){
	return abs(pos[0]) + abs(pos[1]);
}

class ManhattanCompare{
public:
	bool operator() (const array<int, 2>& lhs, const array<int, 2>& rhs) const {
		return manhattanDistance(lhs) < manhattanDistance(rhs);
	}
};

int main(){

	ifstream inputFile("Day03.txt");
	string line;
	vector<string> firstPath;
	vector<string> secondPath;
	unordered_set<array<int, 2>, boost::hash<array<int, 2>>> firstWire;
	unordered_set<array<int, 2>, boost::hash<array<int, 2>>> secondWire;
	set<array<int, 2>, ManhattanCompare> intersections;


	getline(inputFile, line);
	boost::split(firstPath, line, [](char c){return c == ',';});

	getline(inputFile, line);
	boost::split(secondPath, line, [](char c){return c == ',';});

	array<int, 2> loc {0, 0};
	for (auto move : firstPath){
		char dir = move[0];
		int steps = stoi(move.substr(1));
		if (dir == 'R'){
			for (int i = 1; i <= steps; i++){
				loc[0]++;
				firstWire.insert(loc);
			}
		}
		else if (dir == 'L'){
			for (int i = 1; i <= steps; i++){
				loc[0]--;
				firstWire.insert(loc);
			}
		}
		else if (dir == 'U'){
			for (int i = 1; i <= steps; i++){
				loc[1]++;
				firstWire.insert(loc);
			}
		}
		else {
			for (int i = 1; i <= steps; i++){
				loc[1]--;
				firstWire.insert(loc);
			}
		}
	}

	loc[0] = 0;
	loc[1] = 0;
	for (auto move : secondPath){
		char dir = move[0];
		int steps = stoi(move.substr(1));
		if (dir == 'R'){
			for (int i = 1; i <= steps; i++){
				loc[0]++;
				secondWire.insert(loc);
			}
		}
		else if (dir == 'L'){
			for (int i = 1; i <= steps; i++){
				loc[0]--;
				secondWire.insert(loc);
			}
		}
		else if (dir == 'U'){
			for (int i = 1; i <= steps; i++){
				loc[1]++;
				secondWire.insert(loc);
			}
		}
		else {
			for (int i = 1; i <= steps; i++){
				loc[1]--;
				secondWire.insert(loc);
			}
		}
	}

	for (auto pos : firstWire){
		if (secondWire.find(pos) != secondWire.end()){
			intersections.insert(pos);
		}
	}

	cout << manhattanDistance(*intersections.begin()) << endl;
}