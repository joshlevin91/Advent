#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <boost/algorithm/string.hpp>

using namespace std;

// Find shortest distance between locations: brute force computation of every permutation
int main(){

	ifstream inputFile ("input.txt");
	string line;
	vector<string> tokens;
	vector<string> locations;
	map<pair<string, string>, int> distances;
	vector<vector<string>> locPerms;
	int shortestDist = 0;
	int longestDist = 0;

	// Read in locations and map two locations to distance between them
	while(getline(inputFile, line)){

		boost::split(tokens, line, [](char c){return c == ' ';});

		for(int i = 0; i <= 2; i += 2){
			if(find(locations.begin(), locations.end(), tokens[i]) == locations.end()){
				locations.push_back(tokens[i]);
			}
		}

		distances[make_pair(tokens[0], tokens[2])] = stoi(tokens[4]);
	}

	// Find all permutations of locations
	do {

		vector<string> tempLocPerm;
		for(string loc : locations){
			tempLocPerm.push_back(loc);
		}
		locPerms.push_back(tempLocPerm);
	} while (next_permutation(locations.begin(), locations.end()));

	// Find shortest sum distance of each permutation
	for (vector<string> loc : locPerms){
		int tempTotal = 0;
		for (int i = 1; i < loc.size(); i++){
			if (distances.find(make_pair(loc[i-1],loc[i])) != distances.end()){
				tempTotal += distances[make_pair(loc[i-1],loc[i])];
			}
			else {
				tempTotal += distances[make_pair(loc[i],loc[i-1])];
			}
		}
		if (shortestDist == 0 | tempTotal < shortestDist){
			shortestDist = tempTotal;
		}
		if (tempTotal > longestDist){
			longestDist = tempTotal;
		}
	}
	cout << "Shorest distance = " << shortestDist << endl;
	cout << "Longest distance = " << longestDist << endl;
}