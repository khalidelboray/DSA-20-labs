use strict;
use warnings;
use JSON;

my @names = qw(ali ahmed ibrahim islam fatma fahim fadi);
my %dic;
for my $name (@names) {
    my $let = [split('',$name)]->[0];
    push @{$dic{$let}} , $name;
}
print encode_json  \%dic;