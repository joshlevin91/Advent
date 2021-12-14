#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;
using Board = vector<vector<pair<int, bool>>>;

void mark_board(Board& board, const int ncheck) {
    for (auto& row : board) {
        for (auto& n : row) {
            if (n.first == ncheck) {
                n.second = true;
            }
        }
    } 
}

int compute_score(const Board board, const int n) {
    int sum = 0;
    for (auto& row : board) {
        for (auto& n : row) {
            if (n.second == false) {
                sum += n.first;
            }
        }
    }
    return sum*n;
}

bool check_board_for_bingo(const Board board) {
    // Check rows
    for (int i = 0; i < board.size(); i++) {
        bool bingo = true;
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j].second == false) {
                bingo = false;
                break;
            }
        }
        if (bingo)  {
            return true;
        }
    }

    // Check columns
    for (int i = 0; i < board[0].size(); i++) {
        bool bingo = true;
        for (int j = 0; j < board.size(); j++) {
            if (board[j][i].second == false) {
                bingo = false;
                break;
            }
        }
        if (bingo)  {
            return true;
        }
    }
    return false;
}

int main(){
	ifstream inputFile ("Day04.txt");
	string line;
    vector<int> numbers;
    vector<Board> boards;

    bool first = true;
    Board board;
	while(getline(inputFile, line)){
        if (first) {
            string sn;
            stringstream temp(line);
            while(getline(temp, sn, ',')) {
                numbers.push_back(stoi(sn));
            }
            first = false;
        }
        else if (line.empty()) {
            boards.push_back(board);
            board.clear();
        }
        else {
            string sn;
            stringstream temp(line);
            vector<pair<int, bool>> row;
            while(getline(temp, sn, ' ')) {
                if (!any_of(sn.begin(), sn.end(), ::isdigit)) continue;
                row.push_back(make_pair(stoi(sn), false));
            }      
            board.push_back(row);    
        }
	}
    boards.push_back(board);

    bool bingo = false;
    for (auto n : numbers) {
        // Mark boards
        for (auto& board : boards) {
            mark_board(board, n);
        }

        // Check boards for bingo 
        for (int i = 1; i < boards.size(); i++) {
            if (check_board_for_bingo(boards[i])) {
                cout << compute_score(boards[i], n) << endl;
                bingo = true;
                break;
            }
        }
        if (bingo) {
            break;
        }
    }
}
