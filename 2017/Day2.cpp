#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    string row;
    ifstream inputFile("Day2.txt");
    int checksum = 0;
    int divsum = 0;

    while (getline(inputFile, row)){

        istringstream iss(row);
        string word;
        vector<int> numbers;

        while(iss >> word) {
            numbers.push_back(stoi(word));
        }

        //p1
        int min = 100000000;
        int max = -1;
        for (int n : numbers){
            if (n > max){
                max = n;
            }
            if (n < min) {
                min = n;
            }
        }
        checksum += max - min;

        //p2
        for (int n : numbers){
            for (int m : numbers){
                if (n == m){
                    continue;
                }
                if (n % m == 0){
                    divsum += n / m;
                }
            }
        }
    }
    cout << checksum << endl;
    cout << divsum << endl;
}