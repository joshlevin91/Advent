#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){

	ifstream inputFile ("Day03.txt");
	string line;

  int line_count = 0;
  vector<int> ones;
	while(getline(inputFile, line)){
    ones.resize(line.length());
    for (int i = 0; i < line.length(); i++) {
      if (line[i] == '1') {
        ones[i]++;
      }
    }
    line_count++;
	}
  
  string gr;
  string er;
  for (auto n : ones) {
    if (n > line_count/2) {
      gr.push_back('1');
      er.push_back('0');
    } else {
      gr.push_back('0');
      er.push_back('1');
    }
  }

  int grd = stoi(gr, nullptr, 2);
  int erd = stoi(er, nullptr, 2);

  cout << grd*erd << endl;

}