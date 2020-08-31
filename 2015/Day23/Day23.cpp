#include <fstream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <iostream>

using namespace std;

ifstream inputFile ("input.txt");
string line;
vector<string> tokens;
vector<vector<string>> instructions;

int main(){
	while(getline(inputFile, line)){

		boost::split(tokens, line, [](char c){return c == ' ';});
		instructions.push_back(tokens);
	}

	int a = 1;
	int b = 0;

	int i = 0;
	while (i < instructions.size()){

		string instruction = instructions[i][0];

		if (instruction == "hlf"){

			if (instructions[i][1] == "a"){
				a /= 2;
			}
			else {
				b /= 2;
			}
		}
		else if (instruction == "tpl"){

			if (instructions[i][1] == "a"){
				a *= 3;
			}
			else {
				b *= 3;
			}
		}
		else if (instruction == "inc"){

			if (instructions[i][1] == "a"){
				a++;
			}
			else {
				b++;
			}		
		}
		else if (instruction == "jmp"){

			string sign = instructions[i][1].substr(0,1);
			int jump = stoi(instructions[i][1].substr(1));

			if(sign == "+"){
				i += jump;
			}
			else{
				i -= jump;
			}
			continue;
		}
		else if (instruction == "jie"){
			
			string reg = instructions[i][1].substr(0,1);
			string sign = instructions[i][2].substr(0,1);
			int jump = stoi(instructions[i][2].substr(1));

			if ((reg == "a" & a%2 == 0) | (reg == "b" & b%2 == 0)){
				if(sign == "+"){
					i += jump;
				}
				else{
					i -= jump;
				}
				continue;
			}
		}
		else if (instruction == "jio"){

			string reg = instructions[i][1].substr(0,1);
			string sign = instructions[i][2].substr(0,1);
			int jump = stoi(instructions[i][2].substr(1));

			if ((reg == "a" & a == 1) | (reg == "b" & b == 1)){
				if(sign == "+"){
					i += jump;
				}
				else{
					i -= jump;
				}
				continue;
			}		
		}

		i++;
	}

	cout << "Value in register b: " << b << endl;
}