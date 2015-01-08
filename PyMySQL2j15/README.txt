chmod 700 something.pem
ssh -i something.pem ubuntu@ipadd

My Folders with Files that are published are stored in /var/www/html
For example, /var/www/html/ipynbv path leads to files that are currently published (as of today, 2 Jan 2015).

Locally, make an ipython notebook file.
`ipython nbconvert somefile.ipynb`
This command will convert ipynb files into html files by default. We can also specify format depending on our need.
For instance, the command below will convert a ipynb file into a markdown file. 
`ipythin nbconvert to --markdown somefile.ipynb`

Now from local path where our new ipython notebook file is created, we need to copy this into AWS folder /home/ubuntu 
(Or we can also copy them directly into the folder where other published files live)

`scp -i something.pem somefile.html ubuntu@ipadd:/home/ubuntu`

This will send the newly created html file to the AWS folders. Now from the AWS server, sudo-copy this new html file into /var/www/html/ipynbv
That's it, refresh the website, and there I can see the new html page at: http://pyas.me/ipynbv/somefile.html
