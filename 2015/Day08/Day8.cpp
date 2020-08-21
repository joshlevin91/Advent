#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <array>

using namespace std;

void removeEscSeq(string& s);

int main(){

	ifstream inputFile ("input.txt");
	string line;
	int nCode = 0;
	int nMem = 0;

	while (getline(inputFile, line)){

		nCode += line.length();
		removeEscSeq(line);
		nMem += line.length();
	}

	cout << "Answer: " << nCode - nMem << endl;
}


void removeEscSeq(string& s){

	array<string,16> escSeq {"\\a", "\\b", "\\e", "\\f", "\\n", "\\r", "\\t", "\\v",
                             "\\\\", "\\\'", "\\\"", "\\?", "\\nnn", "\\xhh…", 
                             "\\uhhhh", "\\Uhhhhhhhh"};

	for (auto it = escSeq.begin(); it != escSeq.end(); ++it){

		string::size_type i = s.find(*it);

    	while (i != string::npos) {

    		s.erase(i, (*it).length());
    		i = s.find(*it, i);
    	}
	}
}