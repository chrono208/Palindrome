# Palindrome

<h1>Overview</h1>
The palindrome() function checks whether a given word or phrase is a palindrome — meaning it reads the same backward as forward.<br>
It reverses the input string manually and compares the reversed version to the original.<br>

<h2>How it works</h2>
<ul>
<li>The input string is stored in word.</li>
<li>A new empty string reversedWord is created.</li>
<li>The function loops through param[::-1], which iterates through the string in reverse order.</li>
<li>Each letter from the reversed string is appended to reversedWord.</li>
<li>After the loop, it compares word and reversedWord:</li>
  <ul>
    <li>If they are identical, the function returns True.</li>
    <li>Otherwise, it returns False.</li>
  </ul>
</ul>


<h3>Example</h3>
result = palindrome("racecar")
print(result)

<h3>Output</h3>
True


<h3>Example 2</h3>
result = palindrome("hello")
print(result)

<h3>Output 2</h3>
False
