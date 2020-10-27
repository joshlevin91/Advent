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

		int adj_digits = 0;
		int ad_counter = 0;
		bool never_decreases = true;

		for (string::size_type i = 1; i < str_num.size(); i++){

			// Count number of adjacent duplicate digits
			if (str_num[i] == prev_char){
				adj_digits++;
			}
			// Reset if not duplicates
			else {
				adj_digits = 0;
			}

			// If two adjacent duplicate digits, increase counter
			if (adj_digits == 1){
				ad_counter ++;
			}
			// If there is a third adjacent duplicate digit, decrease counter
			else if (adj_digits == 2){
				ad_counter--;
			}

			// Check if numbers decrease
			if (never_decreases && str_num[i] < prev_char){
				never_decreases = false;
			}

			prev_char = str_num[i];
		}

		if (ad_counter > 0 && never_decreases){
			n_pw++;
		}
	}

	cout << n_pw << endl;
}