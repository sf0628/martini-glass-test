# Martini Glass Test
a martini glass in ASCII form

## Execution
type “python martini.py <arg>” in command line

## How it works
A user will input a number describing the width of the top of the martini glass and a full martini glass should be created.

## Program Specifications
* The program should take a single integer argument, representing the width of the top of the glass, designated ‘n’. 
* The bowl of glass should be composed of ‘%’ characters. It should be ‘n’ characters wide at the top, and 1 character wide at 
  the bottom. Each row should be filled with ‘%’ characters
* The bowl of the martini glass should narrow by 2 characters with every row, unless there are exactly 2 characters in the preceding 
  row. In that case the next row should have 1 character. 
* The martini glass should be left-biased. If an even number is submitted, the stem should  be drawn on column (n / 2)-1, e.g 
  if n=4, it would draw on the 2nd column. 
* The stem of the glass should be drawn of ‘|’ (pipe) characters, be 1 character wide, and ‘n’ characters in height. 
* The base of the glass should be composed of ‘=’ characters, be ‘n’ characters wide, and 1 character tall. 
* The program should error if given no argument, or an argument that is not a number.
* The program should output nothing if given an invalid numeric argument
