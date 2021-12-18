#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <utility>
#include <regex>
#include <set>

using coord = std::pair<int, int>;

int main(){
	std::ifstream inputFile ("Day05.txt");
	std::string line;
    std::map<coord, int> vents;
    int count = 0;

	while(getline(inputFile, line)){
        std::regex rgx("(\\d+),(\\d+) -> (\\d+),(\\d+)");
        std::smatch match;
        std::regex_search(line, match, rgx);
        int x1 = std::stoi(match.str(1));
        int y1 = std::stoi(match.str(2));
        int x2 = std::stoi(match.str(3));
        int y2 = std::stoi(match.str(4));
        // std::cout << x2 << std::endl;

        if (x1 == x2) {
            int ymin = y1;
            int ymax = y2;
            if (y1 > y2) {
                ymin = y2;
                ymax = y1;
            }
            for (int y = ymin; y <= ymax; y++) {
                coord c = std::make_pair(x1, y);
                if (!vents.count(c)) {
                    vents[c] = 1;
                } else {
                    if (vents[c] == 1) {
                        count++;
                    }
                    vents[c]++;
                }
            }
        } else if (y1 == y2) {
            int xmin = x1;
            int xmax = x2;
            if (x1 > x2) {
                xmin = x2;
                xmax = x1;
            }
            for (int x = xmin; x <= xmax; x++) {
                coord c = std::make_pair(x, y1);
                if (!vents.count(c)) {
                    vents[c] = 1;
                } else {
                    if (vents[c] == 1) {
                        count++;
                    }
                    vents[c]++;
                }
            }       
        }
	}
    
    std::cout << count << '\n';
}
