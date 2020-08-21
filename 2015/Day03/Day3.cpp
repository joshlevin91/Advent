#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <set>

using namespace std;

void addToVisitedHouses(const char& c, array<int, 2>& location, set<array<int, 2>>& housesVisited);

int main(){

	array<int, 2> santaLocation = {0, 0};
	array<int, 2> roboSantaLocation = {0, 0};
	set<array<int, 2>> housesVisited;

	string line;
	ifstream inputFile ("input.txt");

	int counter = 0;

  	while (getline(inputFile, line)){
  		for(const char& c : line){
  			if (counter % 2 == 0){
  				addToVisitedHouses(c, santaLocation, housesVisited);
  			}
  			else{
  				addToVisitedHouses(c, roboSantaLocation, housesVisited);
  			}
  			counter++;
  		}
  	}

  	cout << "Number of houses visited: " << housesVisited.size() << endl;

	return 0;
}

void addToVisitedHouses(const char& c, array<int, 2>& location, set<array<int, 2>>& housesVisited){
	if (c == '^'){
		location[0]++;
	}
	else if (c == 'v'){
		location[0]--;
	}
	else if (c == '>'){
		location[1]++;
	}
	else if (c == '<'){
		location[1]--;
	}

	housesVisited.insert(location);
}
