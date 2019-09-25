use strict;
use warnings;
use Data::Dumper;

print "Input start num : ";
my $num = <>;
my @list;
for my $i (1 .. $num) {
    my @table;
    for my $k (1 .. $i) {
        push @table , $k * $i;
    }
    push @list , \@table;
}
print Dumper(@list);