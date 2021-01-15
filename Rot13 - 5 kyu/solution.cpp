#include <string>
using namespace std;

string rot13(string msg)
{
  string alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
  string alphabet2 ="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
  string res = "";
  for(int i = 0; i < msg.length();i++)
  {
    char c = msg[i];
    if (alphabet.find(c) != std::string::npos)
    {
      res += alphabet[alphabet.find(c)+13];
    }else if (alphabet2.find(c) != std::string::npos)
    {
      res += alphabet2[alphabet2.find(c)+13];
    }else{
      res += c;
    }
  }

  return res;
}
