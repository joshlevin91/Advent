#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>

using namespace std;

struct Reindeer
{
	string name;
	int speed;
	int flightTime;
	int restTime;
	int totalTime;
	int totalDist;
};

Reindeer getReindeer(string line);
int getFlightDistance(Reindeer reindeer, int time);

int main(){

	ifstream inputFile ("input.txt");
	string line;
	int longestDistance = 0;
	int t = 2503;

	while(getline(inputFile, line)){

		Reindeer newReindeer = getReindeer(line);

		int newDistance = getFlightDistance(newReindeer, t);
		
		if (newDistance > longestDistance){
			longestDistance = newDistance;
		}
	}

	cout << "The winning reindeer travelled " << longestDistance << " kms." << endl;
}

Reindeer getReindeer(string line){

	Reindeer newReindeer;
	vector<string> tokens;

	boost::split(tokens, line, [](char c){return c == ' ';});

	newReindeer.name = tokens[0];
	newReindeer.speed = stoi(tokens[3]);
	newReindeer.flightTime = stoi(tokens[6]);
	newReindeer.restTime = stoi(tokens[13]);
	newReindeer.totalTime = newReindeer.flightTime + newReindeer.restTime;
	newReindeer.totalDist = newReindeer.speed*newReindeer.flightTime;

	return newReindeer;
}

int getFlightDistance(Reindeer reindeer, int time){
	div_t divResult = div(time, reindeer.totalTime);
	int d1 = divResult.quot*reindeer.totalDist;
	int d2 = 0;
	if (divResult.rem >= reindeer.flightTime){
		d2 = reindeer.totalDist;
	}
	else {
		d2 = divResult.rem*reindeer.speed;
	}
	return d1 + d2;
}