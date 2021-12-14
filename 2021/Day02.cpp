#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;

int main(){

	ifstream inputFile ("Day02.txt");
	string line;

	int h = 0, d = 0, a = 0;
	while(getline(inputFile, line)){
		std::regex rgx("([a-z]*) (\\d)");
        std::smatch match;
        std::regex_search(line, match, rgx);

        string dir = match.str(1);
        int units = stoi(match.str(2));
        
        if (dir == "forward") {
            h += units;
            d += a*units;
        } else if (dir == "down") {
            a += units;
        } else if (dir == "up") {
            a -= units;
        }
	}
	cout << h*d << endl;
}
