// 2015 Day 1
 
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
 
int main()
{
  int floor = 0;
  int position = 0;
  bool basementFound = false;
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

      position++;

      if(floor < 0 & !basementFound){

        cout << "Floor found at position " << position << endl;
        basementFound = true;

      }
  	}
  }

  inputFile.close();

  cout << "Floor #  = " << floor << endl;

  return 0;
}