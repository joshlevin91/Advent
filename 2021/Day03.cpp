#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

char helper(vector<string> bins, int idx) {
  int ones = 0;
  int zeros = 0;
  for (auto bin : bins) {
    if (bin[idx] == '1') {
      ones++;
    } else {
      zeros++;
    }
  }
  if (ones >= zeros) {
    return '1';
  }
  return '0';
}

int main(){

	ifstream inputFile ("Day03.txt");
	string line;

  int line_count = 0;
  vector<int> ones;
  vector<string> bins;
	while(getline(inputFile, line)){
    bins.push_back(line);
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
    if (n >= line_count/2) {
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

  //p2 
  vector<string> bins2(bins);
  {
    int i = 0;
    while (bins.size() > 1) {
      int j = 0;
      char val = helper(bins, i);
      while (j < bins.size()){
        if (bins[j][i] != val) {
          bins.erase(bins.begin()+j);
        } else {
          j++;
        }
      }
      i++;
    }
  }

  int i = 0;
  while (bins2.size() > 1) {
    int j = 0;
    char val = helper(bins2, i);
    while (j < bins2.size()){
      if (bins2[j][i] == val) {
        bins2.erase(bins2.begin()+j);
      } else {
        j++;
      }
    }
    i++;
  }

  cout << stoi(bins[0], nullptr, 2)*stoi(bins2[0], nullptr, 2) << endl;

}