#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <map>

using namespace std;

// Reindeer stats
struct stats
{
	int speed;
	int flightTime;
	int restTime;
	int totalTime;
	int totalDist;
	int points;
	int flightDistance;
};

void addReindeer(map<string, stats>& reindeerMap, string line);
int getFlightDistance(stats reindeerStats, int time);

int main(){

	int time = 2503;

	ifstream inputFile ("input.txt");
	string line;

	// Add reindeers to map
	map<string, stats> reindeers;
	while(getline(inputFile, line)){
		addReindeer(reindeers, line);
	}

	for(int t = 1; t < time; t++){

		int maxFlightDistance = 0;
		string firstPlaceName = "";

		// Check flight distance of each reindeer and add point to furthest reindeer
		for (auto it = reindeers.begin(); it != reindeers.end(); ++it){

			int flightDistance = getFlightDistance(it->second, t);
			it->second.flightDistance = flightDistance;

			if (flightDistance > maxFlightDistance){
				maxFlightDistance = flightDistance;
				firstPlaceName = it->first;
			}
		}
		reindeers[firstPlaceName].points++;
	}

	// Get points of winning reindeer
	int winningPoints = 0;
	for (auto it = reindeers.begin(); it != reindeers.end(); ++it){
		if(it->second.points > winningPoints){
			winningPoints = it->second.points;
		}
	}

	cout << "The winning reindeer has " << winningPoints << " points." << endl;
}

// Add reindeer to map
void addReindeer(map<string, stats>& reindeerMap, string line){

	stats reindeerStats;
	vector<string> tokens;

	boost::split(tokens, line, [](char c){return c == ' ';});

	string name = tokens[0];

	reindeerStats.speed = stoi(tokens[3]);
	reindeerStats.flightTime = stoi(tokens[6]);
	reindeerStats.restTime = stoi(tokens[13]);
	reindeerStats.totalTime = reindeerStats.flightTime + reindeerStats.restTime;
	reindeerStats.totalDist = reindeerStats.speed * reindeerStats.flightTime;
	reindeerStats.points = 0;
	reindeerStats.flightDistance = 0;

	reindeerMap.insert(pair<string, stats>(name, reindeerStats));
}

// Get flight distance of reindeer at some time
int getFlightDistance(stats reindeerStats, int time){
	div_t divResult = div(time, reindeerStats.totalTime);
	int d1 = divResult.quot * reindeerStats.totalDist;
	int d2 = 0;
	if (divResult.rem >= reindeerStats.flightTime){
		d2 = reindeerStats.totalDist;
	}
	else {
		d2 = divResult.rem * reindeerStats.speed;
	}
	return d1 + d2;
}