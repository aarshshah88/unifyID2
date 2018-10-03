# unifyID2

Why might this score be completely wrong?
This score could potentially be wrong for many reasons. For one there could be many other factors involved with creating a score that actually represents the likelihood of the a request being fraudulent. For example the source, the source's previous requests, the frequency of requests from the source and so much more. In addition we are trusting an API to get us the longitude and latitudes off which we are basing our distance formula. I found on a few occasions that for a given IP address the API and a quick google search gave different coordinates. Even one mistake here can mis identify the closest IPaddress request and if that close one was Fraudulent we would be multiplying by 2 for no reason. Also multiplying by 2 is fairly arbitrary, ideally we would be able to figure out weights of different features that are important and then use those weights to calculate a score. 

What challenges are there with computing distances based on long/lat?
well for one you have to have latitude and longitude being very precise and accurate. Then calculating the mileage based on the longitude and latitude is dfficult because different distance formulas take into account different aspects of the earth. Different formulas account for the earths "roundness' in different ways and some don't account for it all. There isn't a super standard way and if long/lat are inacccurate even once the whole algorithm can get messed up.

Improvements:

Currently we are storing all the rules on a file, so the space complexity for the current algorithm is 0(n) since we are storing all the objects for each IP address in a list. We need all of those to compare with the current input so it would be hard to reduce that, however the current runtime of 0(n) can be improved signifcantly. Currently we are comparing the input distance to every rule. With many input requests, and as the file grows longer this isn't great performance. We can use sorting based on some distance metric and then binary search on the list to bring this down to 0{logn) or we can use a balanced binary tree with a comparision function that also uses somem sort of distance metric to find the closest previous IP address request. 

Testing:
In order to test the file, just change the IP address on the input file (this file should always only have 1 line). Then run the file by either opening it up in a text editor, or running the file as a script by calling python UnifyID.py from terminal.

