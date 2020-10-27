#include <iostream>
#include <string>

using namespace std;

int main(){

	const int start = 271973;
	const int end = 785961;
	int n_pw = 0;

	for (int i = start; i <= end; i++){

		string str_num = to_string(i);
		char prev_char = str_num[0];

		bool adj_digits = false;
		bool never_decreases = true;

		for (string::size_type i = 1; i < str_num.size(); i++){

			if (!adj_digits && str_num[i] == prev_char){
				adj_digits = true;
			}

			if (never_decreases && str_num[i] < prev_char){
				never_decreases = false;
			}

			prev_char = str_num[i];
		}

		if (adj_digits && never_decreases){
			n_pw++;
		}
	}

	cout << n_pw << endl;
}