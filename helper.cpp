#include <iostream>
#include <vector>
using namespace std;

class Board {
  public:
    vector<vector<char>> board;
    Board() {
        vector<char> a = {'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'}, b, c, d, e = {'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'};
        for (int i = 0; i < 8; i++) b.push_back('p');
        for (int i = 0; i < 8; i++) c.push_back('_');
        for (int i = 0; i < 8; i++) d.push_back('P');
        board.push_back(a);
        board.push_back(b);
        for (int i = 0; i < 4; i++) board.push_back(c);
        board.push_back(d);
        board.push_back(e);
    }

    vector<vector<char>> get_initial_board() {}
};

int evaluate(Board position) {
    int score = 0;
    return score;
}

class Node {
  public:
    Board board;
    int eval;
    Node* prev_position;
    vector <Node*>next_positions;
    string turn;

    Node(Board new_position, Node* current, string colour_to_play) {
        board = new_position;
        prev_position = current;
        turn = colour_to_play;
        eval = evaluate(board);
    }
};

class Tree {
  public:
    Node *root_p;
    Tree() {
        root_p = NULL;
    }
};