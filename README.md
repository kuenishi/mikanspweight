mikanspweight
=============

Set up
------

 + Install Net::Twitter::Lite and Net::OAuth perl modules.

   <pre>
    # apt-get install libnet-twitter-lite-perl
    # apt-get install libnet-oauth-perl
   </pre>

 + Get following information from @moritapo

   * Consumer key
   * Consumer secret
   * Access token
   * Access token secret

   Now you can retweet the latest mikansp weight with the following command:

   <pre>
    $ ./rt-mweight.pl 'consumer key' 'consumer secret' 'access token' 'access token secret'
   </pre>

   Enjoy!


Automate retweets
-----------------

 + Create /etc/cron.hourly/rt-mweight with permission 755

   <pre>
   #!/bin/sh
   
   /installed/path/rt-mweight.pl 'consumer key' 'consumer secret' 'access token' 'access token secret'
   </pre>


TODO items
----------

 + Read the next timeline if we cannot find the latest mweight in the
   first page.
 + Avoid having secret tokens as plain text.
 + Daemonize rt-mweight.pl.
 + Implement more interesting features rather than simple retweeting.

mikanspweight.py
================

 + Deflate the file consumer.zip

 + Login with your default browser

 + do the follwoing sequence:

 <pre>
 $ virtialenv .
 $ source bin/activate
 $ pip install twitter
 $ python rt_mweight.py
 </pre>

 + Then your default browser starts and authorize mikanspweight

 + Copy the PIN code

 + Paste to the command line

 + Enjoy the timeline from streaming of @mikansp.


TODO
----

 + forecast

refs
----

 + https://dev.twitter.com/docs/api/2/get/user

 + https://dev.twitter.com/docs/api/1/post/statuses/retweet/%3Aid
