# Python-Programs
Programs solved as part of python training from Udemy.

First program- Decode Matrix

This program is to decode a matrix.The matrix script is a  N*M  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
The matrix should be decoded by reading the column from top to bottom.If there are symbols or spaces between two alphanumeric characters of the decoded script, then replace them with a single space '' for better readability.
Sample Input
7 3
Tsi
h%x
i #
sM
$a
#t%
ir!
Sample Output
This is Matrix#  %!

Second Program- Maximise it

Given a function f(x)= X**2, also given a list of k elements. maximise it gives
S=(f(x1)+f(x2)+....+f(xk))%M
Find the maximum value of S

Input Format

The first line contains 2 space separated integers  which is the no of lists to be entered and the M value
Then input the elements in the list

Sample Input
3 1000 ( 3 lists, M value is 1000)
2 5 4   (1st list contain 2 elements- 5,4)
3 7 8 9 (2nd list contain 3 elements-7,8,9)
5 5 7 8 9 10 (3rd list contain 5 elements-5,7,8,9,10)

Sample Output
206

Third Program - Airport Gate

At an airport you have a timetable for arrivals and departures.
You need to determine the minimum number of gates you*d need to provide so that all the planes can be placed at a gate as per their schedule.
The arrival and departure times for each plane are presented in two arrays, sorted by arrival time, and you're told the total number of flights for the
day. Assume that no planes remain overnight at the airport; all fly in and back out on the same day. Assume that if a plane departs in the same minute as another plane arrives, the arriving plane takes priority (i.e. you'll still need the gate for the departing plane). Write a program that returns
the minimum number of gates needed for the schedules you're given.
 Example:
 * arrQ = {900, 940, 950, 1100,1500,1800}
 * depQ = {910,1200,1120, 1130,1900, 2000}
 * flights = 6