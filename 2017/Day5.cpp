#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string offset;
    ifstream inputFile("Day5.txt");
    vector<int> offsets;
    int pos = 0;

    while (getline(inputFile, offset)){
        offsets.push_back(stoi(offset));
    }

    int n = 0;
    while (pos < offsets.size()){
        int prev_pos = pos;
        pos += offsets[pos];
        if (offsets[prev_pos] >= 3){
            offsets[prev_pos]--;
        }
        else {
            offsets[prev_pos]++;
        }
        n++;
    }

    cout << n << endl;
}