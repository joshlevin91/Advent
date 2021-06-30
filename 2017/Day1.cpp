#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string digits;
    ifstream inputFile ("Day1.txt");
    int sum = 0;

    while (getline(inputFile, digits)){
        int l = digits.length();
        int step = l/2;

        for (int i = 0; i < l; i++){
            int j = (i + step) % l;

            if (digits[i] == digits[j]){
                int digit = digits[i] - '0';
                sum += digit;
            }
        }
    }
    
    cout << sum << endl;
}