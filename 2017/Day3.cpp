#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<vector<int>> findNeighbors(vector<int> pos);

int main(){

    int input = 368078;

    vector<int> pos = {0, 0};
    int val = 1;
    map<vector<int>, int> values;
    values[pos] = val;

    char dirs[4] = {'r', 'u', 'l', 'd'};
    int nd = 0;

    int counter = 1;
    int max = 1;
    bool first = false;

    while (val <= input){

        char d = dirs[nd % 4];
        switch (d) {
            case 'r':
                pos[0]++;
                break;
            case 'u':
                pos[1]++;
                break;
            case 'l':
                pos[0]--;
                break;
            case 'd':
                pos[1]--;
                break;
        }

        if (counter % max == 0){
            counter = 0;
            nd++;
            if (!first){
                first = true;
            }
            else {
                max++;
                first = false;
            }
        }

        val = 0;
        vector<vector<int>> neighbors = findNeighbors(pos);
        for (vector<int> n : neighbors){
            if (values.find(n) != values.end()){
                val += values[n];
            }
        }
        values[pos] = val;

        counter++;
    }
    cout << val << endl;
}

vector<vector<int>> findNeighbors(vector<int> pos){

    vector<vector<int>> neighbors;

    neighbors.push_back({pos[0]+1, pos[1]});
    neighbors.push_back({pos[0]+1, pos[1]+1});
    neighbors.push_back({pos[0]+1, pos[1]-1});
    neighbors.push_back({pos[0]-1, pos[1]});
    neighbors.push_back({pos[0]-1, pos[1]+1});
    neighbors.push_back({pos[0]-1, pos[1]-1});
    neighbors.push_back({pos[0],   pos[1]+1});
    neighbors.push_back({pos[0],   pos[1]-1});
    
    return neighbors;
}