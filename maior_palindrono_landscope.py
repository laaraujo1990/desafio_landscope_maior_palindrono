"""
Searching Challenge
Have the function SearchingChallenge(str) take the str parameter being passed and 
find the longest palindromic substring, which means the longest substring which is 
read the same forwards as it is backwards. For example: if str is "abracecars" then 
your program should return the string racecar because it is the longest palindrome 
within the input string.

The input will only contain lowercase alphabetic characters. The longest palindromic 
substring will always be unique, but if there is none that is longer than 2 characters, 
return the string none.

Examples
Input: "hellosannasmith"
Output: sannas
Input: "abcdefgg"
Output: none
"""

def SearchingChallenge(strParam):

  strParam = strParam.lower()
  results = []
  resp = 'none'
  for i in range(len(strParam)):
    for j in range(0, i):
      chunk = strParam[j:i + 1]

      if chunk == chunk[::-1]:
        results.append(chunk)
        resp = max(results)
  if len(resp) < 3:
    resp = 'none'

  return resp

# keep this function call here 
print(SearchingChallenge(input()))
