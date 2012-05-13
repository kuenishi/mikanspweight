mikanspweight
=============

Set up
------

 + Go to https://dev.twitter.com/ and press 'Create an app'.

 + Fill information and then press 'Create your Twitter application'.

 + Move to 'Settings' tab and change your application type to 'Read and Write'.

 + Move to 'Details' tab and press 'Create my access token'.

 + Write down

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
