It handles GET as a webserver should but I didn't whether that was 
the same as the GET method in forms (like POST) so I didn't implement that. It wouldn't 
be hard to do. Just split on '?' and then split that on '&' and then on '='. I've done it
in Perl and C++ before.

The only thing that must be changed to work is in the Config file
The first line is the ROOT folder (full path is required)
The second line is the port

I close the port on a key-stroke so just Ctrl-C at the end.

Google API is a bit buggy so it won't let you test it more than a few times per time interval. 

I must attribute my code to various tutorials online. There isn't any one peice of code I can point to that was ripped off but it was a lot of putting together
different things that seemed to be working.

The Unit Test just starts up the webserver. I included a sample directory with an index.html and a text file. I didn't know how to Unit Test that it displayed in the browser.
