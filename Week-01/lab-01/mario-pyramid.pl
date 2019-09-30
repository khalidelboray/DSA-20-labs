use strict;
use warnings;

print "Input number : ";
chomp(my $num = <>);
for my $i (0..$num) {
    print ' ' x ($num - $i );
    print '*' x $i , "\n";
}