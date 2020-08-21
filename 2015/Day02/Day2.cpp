// 2015 Day 2
 
#include <iostream>
#include <fstream>
#include <string>
#include <boost/algorithm/string.hpp>
#include <vector>
#include <algorithm>

using namespace std;
 
int main()
{
  vector<int> dims(3, 0);
  int s1, s2, s3, smallestSide;
  int surfaceArea = 0;
  int ribbon = 0;

  string line;
  vector<string> dimString;
  ifstream inputFile ("input.txt");

  while (getline(inputFile, line)){
    boost::split(dimString, line, boost::is_any_of("x"));

    dims[0] = std::stoi(dimString[0]);
    dims[1] = std::stoi(dimString[1]);
    dims[2] = std::stoi(dimString[2]);

    s1 = dims[0]*dims[1];
    s2 = dims[1]*dims[2];
    s3 = dims[2]*dims[0];

    // Surface Area
    smallestSide = min({s1, s2, s3});

    surfaceArea += 2*s1 + 2*s2 + 2*s3 + smallestSide;

    // Ribbon
    sort(dims.begin(), dims.begin()+3);

    ribbon += 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2];
  }

cout << "Total square feet of wrapping paper to order: " << surfaceArea << endl;
cout << "Total length of ribbon to order: " << ribbon << endl;

  return 0;
}