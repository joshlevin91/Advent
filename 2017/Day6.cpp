#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int maxIndex(vector<int> numbers);

int main()
{
    ifstream inputFile("Day6.txt");
    string blocks;
    vector<int> config;
    vector<vector<int>> configs;

    // Get input configuration
    while (getline(inputFile, blocks)){
        istringstream iss(blocks);
        int block;
        while (iss >> block){
            config.push_back(block);
        }
    }

    // Find number of cycles before duplication
    int cycles = 0;
    while (find(configs.begin(), configs.end(), config) == configs.end()) {
        configs.push_back(config);

        int idx = maxIndex(config);
        int max = config[idx];
        config[idx] = 0;

        for (int j = 1; j <= max; j++){
            int next_idx = (idx + j) % config.size();
            config[next_idx]++;
        }
        cycles++;
    }
    
    // Find index of configuration seen before
    int idx_first = distance(configs.begin(), find(configs.begin(), configs.end(), config));

    cout << cycles << endl;
    cout << cycles - idx_first << endl;
}

int maxIndex(vector<int> numbers){
    int max_index = 0;
    int max = numbers[0];
    for (int i = 1; i < numbers.size(); i++){
        if (numbers[i] > max){
            max = numbers[i];
            max_index = i;
        }
    }
    return max_index;
}