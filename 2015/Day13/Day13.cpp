#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <boost/algorithm/string.hpp>

using namespace std;

// Find optimal total change in happiness: brute force computation of every permutation
int main(){

	ifstream inputFile ("input.txt");
	string line;
	vector<string> tokens;
	vector<string> names;
	map<pair<string, string>, int> hUnits;
	vector<vector<string>> namePerms;
	int totalUnits = 0;

	// Read in names and map two names to happiness units
	while(getline(inputFile, line)){

		boost::split(tokens, line, [](char c){return c == ' ';});

		string firstName = tokens[0];
		string secondName = tokens[10].substr(0, tokens[10].size()-1); //Strip '.' from second name

		if(find(names.begin(), names.end(), firstName) == names.end()){
			names.push_back(firstName);
		}
		if(find(names.begin(), names.end(), secondName) == names.end()){
			names.push_back(secondName);
		}

		int hUnitPair = stoi(tokens[3]);
		if(tokens[2] == "lose"){
			hUnitPair = -hUnitPair;
		}
		
		if (hUnits.find(make_pair(secondName, firstName)) == hUnits.end()){
			hUnits[make_pair(firstName, secondName)] = hUnitPair;
		}
		else {
			hUnits[make_pair(secondName, firstName)] += hUnitPair;
		}

	}

	// Find all permutations of names
	do {
		vector<string> tempLocPerm;
		for(string loc : names){
			tempLocPerm.push_back(loc);
		}
		namePerms.push_back(tempLocPerm);
	} while (next_permutation(names.begin(), names.end()));

	// Find optimal total change in happiness units
	for (vector<string> loc : namePerms){
		int tempTotal = 0;
		for (int i = 1; i < loc.size(); i++){
			if (hUnits.find(make_pair(loc[i-1],loc[i])) != hUnits.end()){
				tempTotal += hUnits[make_pair(loc[i-1],loc[i])];
			}
			else {
				tempTotal += hUnits[make_pair(loc[i],loc[i-1])];
			}
		}

		if (hUnits.find(make_pair(loc.back(),loc[0])) != hUnits.end()){
			tempTotal += hUnits[make_pair(loc.back(),loc[0])];
		}
		else {
			tempTotal += hUnits[make_pair(loc[0],loc.back())];
		}

		if (tempTotal > totalUnits){
			totalUnits = tempTotal;
		}
	}

	cout << "Total change in happiness = " << totalUnits << endl;
}