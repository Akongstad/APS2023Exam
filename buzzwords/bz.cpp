#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int ALPHABET_SIZE = 26;

struct Node
{
    Node *children[ALPHABET_SIZE];
    int count = 0;
    int depth = 0;

    Node()
    {
        for (int i = 0; i < ALPHABET_SIZE; ++i)
            children[i] = nullptr;
    }

    void insert(const string &str, int index = 0)
    {
        while (index < str.length() && str[index] == ' ')
            index++;
        if (index == str.length())
        {
            count++;
            return;
        }
        else
        {
            count++;
            int letterIndex = str[index] - 'A';
            if (children[letterIndex] == nullptr)
            {
                children[letterIndex] = new Node();
                children[letterIndex]->depth = depth + 1;
            }
            children[letterIndex]->insert(str, index + 1);
        }
    }

    void cleanup()
    {
        for (int i = 0; i < ALPHABET_SIZE; ++i)
        {
            if (children[i] != nullptr)
            {
                children[i]->cleanup();
                delete children[i];
            }
        }
    }

    void calculateCounts(vector<int> &counts)
    {
        counts[depth] = max(count, counts[depth]);
        for (int i = 0; i < ALPHABET_SIZE; ++i)
        {
            if (children[i] != nullptr)
                children[i]->calculateCounts(counts);
        }
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    while (getline(cin, line) && !line.empty())
    {
        Node root;
        for (int i = 0; i < line.length(); ++i)
        {
            if (line[i] != ' ')
                root.insert(line, i);
        }

        vector<int> depths(line.length() + 3, 0);
        root.calculateCounts(depths);
        for (int i = 1; i <= line.length() + 1; ++i)
        {
            if (depths[i] > 1)
                cout << depths[i] << '\n';
            else
            {
                cout << endl;
                break;
            }
        }
    }

    return 0;
}
