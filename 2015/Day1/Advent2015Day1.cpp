// 2014 Day 1
 
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
 
int main()
{
  int floor = 0;
  string line;

  ifstream inputFile ("input.txt");

  while (getline(inputFile, line)){
  	for (auto it = line.cbegin(); it != line.cend(); ++it){
  		if (*it == '('){
  			floor++;
  		}
  		else if (*it == ')'){
  			floor--;
  		}
  	}
  }
  inputFile.close();

  cout << "Floor #  = " << floor << endl;

  return 0;
}