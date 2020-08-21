#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>

using namespace std;

void step(vector<string>& m);
int countOn(const vector<string>& m);

int main(){
	ifstream inputFile ("input.txt");
	string line;
	vector<string> matrix;

	while(getline(inputFile, line)){
		matrix.push_back(line);
	}

	// Set all for corners to on
	matrix[0][0] = '#';
	matrix[matrix.size()-1][0] = '#';
	matrix[0][matrix[0].size()-1] = '#';
	matrix[matrix.size()-1][matrix[0].size()-1] = '#';

	for (int i = 0; i < 100; i++){
		step(matrix);
	}
	
	cout << countOn(matrix) << endl;
}

void step(vector<string>& m){
	vector<string> old_m(m);
	for(int i = 0; i < m.size(); i++){
		for(int j = 0; j < m[0].size(); j++){

			// Count number of neighbors on
			int n_on = 0;
			if(i > 0 && j > 0 && old_m[i-1][j-1] == '#'){
				n_on++;
			}
			if(i > 0 && old_m[i-1][j] == '#'){
				n_on++;
			}
			if(i > 0 && j < m[0].size()-1 && old_m[i-1][j+1] == '#'){
				n_on++;
			}
			if(j > 0 && old_m[i][j-1] == '#'){
				n_on++;
			}
			if(j < m[0].size()-1 && old_m[i][j+1] == '#'){
				n_on++;
			}
			if(i < m.size()-1 && j > 0 && old_m[i+1][j-1] == '#'){
				n_on++;
			}
			if(i < m.size()-1 && old_m[i+1][j] == '#'){
				n_on++;
			}
			if(i < m.size()-1 && j < m[0].size()-1 && old_m[i+1][j+1] == '#'){
				n_on++;
			}

			// Switch condition if on
			if(m[i][j] == '#' & n_on != 2 & n_on != 3 &
				!(i == 0 & j == 0) & !(i == 0 & j == m[0].size()-1) &
				!(i == m.size()-1 & j == 0) & !(i == m.size()-1 && j == m[0].size()-1)){
				m[i][j] = '.';
			}
			// Switch condition if off
			else if (m[i][j] == '.' & n_on == 3){
				m[i][j] = '#';
			}
		}
	}
}

int countOn(const vector<string>& m){
	int n_on = 0;
	for (auto s : m){
		for (auto c : s){
			if (c == '#'){
				n_on++;
			}
		}
	}
	return n_on;
}