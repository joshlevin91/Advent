#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    string passphrase;
    ifstream inputFile("Day4.txt");
    int nvalid = 0;

    while (getline(inputFile, passphrase)){
        istringstream iss(passphrase);
        string password;
        set <string> passwords;

        bool valid = true;
        while (iss >> password){
            sort(password.begin(), password.end());
            if (passwords.find(password) != passwords.end()){
                valid = false;
                break;
            }
            else {
                passwords.insert(password);
            }
        }
        if (valid){
            nvalid++;
        }
    }
    cout << nvalid << endl;
}