#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Node 
{
    Node *children[26]; // A-Z
    int count = 0; // Number of words that end at this node
    int depth = 0; // Depth of this node in the trie

    Node()  
    {
        for (int i = 0; i < 26; ++i)  // Initialize children to nullptr
            children[i] = nullptr;  
    }

    void insert(const string &str, int index = 0)  // Insert string into trie
    {
        while (index < str.length() && str[index] == ' ')  // Skip spaces
            index++;  
        if (index == str.length())  // End of string
        {
            count++;  // Increment count
            return; 
        }

        count++; 
        int letterIndex = str[index] - 'A';  // Convert letter to index

        if (children[letterIndex] == nullptr)  // If child doesn't exist 
        {
            children[letterIndex] = new Node(); // Create child node
            children[letterIndex]->depth = depth + 1;  // Set depth of child node 
        }

        children[letterIndex]->insert(str, index + 1);  // Insert rest of string
    }

    void calculateCounts(vector<int> &counts)  // Calculate counts of repeated words
    {
        counts[depth] = max(count, counts[depth]);  // Update count at depth

        for (int i = 0; i < 26; ++i)  // Recursively calculate counts of children
        {
            if (children[i] != nullptr) 
                children[i]->calculateCounts(counts);  
        }
    }
};

int main()
{
    ios::sync_with_stdio(false);  // Disable sync with C I/O
    cin.tie(nullptr);  // Disable flushing of cout before cin

    string line;  // Input line
    while (getline(cin, line) && !line.empty())  // While input is not empty
    {
        Node root;  // Root of trie
        for (int i = 0; i < line.length(); ++i)  // Insert all words into trie
        {
            if (line[i] != ' ')
                root.insert(line, i);  
        }

        vector<int> depths(line.length() + 3, 0);  // Initialize counts to 0
        root.calculateCounts(depths);  // Calculate counts of repeated words
        for (int i = 1; i <= line.length() + 1; ++i) // Print counts
        {
            if (depths[i] > 1) 
                cout << depths[i] << '\n'; // Print count of repeated words at depth i and newline
            else 
            {
                cout << '\n'; // Print empty line
                break;
            }
        }
    }

    return 0;
}