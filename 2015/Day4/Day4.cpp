#include <iostream>
#include <fstream>
#include <string>
#include <openssl/md5.h>
#include <stdio.h>

using namespace std;

int main(){

	string secretKey;
	string keyToTry;
	unsigned char hash[MD5_DIGEST_LENGTH];
	ifstream inputFile ("input.txt");
	int num = 1;

	getline(inputFile, secretKey);

	while (true) {
		keyToTry = secretKey + to_string(num);
		MD5((unsigned char*) keyToTry.c_str(), (unsigned long) keyToTry.length(), hash);

		// Convert hash to hexidecimal string
		string hashString;
		char buf[MD5_DIGEST_LENGTH];
		for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
		{
		   sprintf(buf, "%02x", hash[i]);
		   hashString.append( buf );
		}

		if (hashString.substr(0,6).compare("000000") == 0){
			break;
		}

		num++;
	}

	cout << num << endl;

	return 0;
}