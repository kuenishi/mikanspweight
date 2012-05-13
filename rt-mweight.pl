#!/usr/bin/perl

use strict;
use warnings;
use utf8;

use Net::Twitter::Lite;

my ($CONSUMER_KEY, $CONSUMER_SECRET, $ACCESS_TOKEN, $ACCESS_TOKEN_SECRET) = @ARGV;

my $t = Net::Twitter::Lite->new(
    consumer_key    => $CONSUMER_KEY,
    consumer_secret => $CONSUMER_SECRET,
    );
$t->access_token($ACCESS_TOKEN);
$t->access_token_secret($ACCESS_TOKEN_SECRET);

my $timeline = $t->user_timeline({screen_name => 'mikansp'});
foreach my $status (@$timeline) {
    my %info = %$status;

    if ($info{'text'} =~ /^My weight/) {
	eval {
	    $t->retweet($info{'id'});
	};
	exit;
    }
}
