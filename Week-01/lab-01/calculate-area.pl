use strict;
no strict 'refs';
use warnings;
use experimental 'smartmatch';

use constant PI    => 4 * atan2(1, 1);

sub triangle {
    return 0.5 * $_[0] * $_[1]
}

sub rectangle {
    return $_[0] * $_[1]
}

sub square {
    return $_[0] ** 2
}

sub circle {
    return PI * ( $_[0] ** 2)
}

my %switcher = (
    't' => "triangle",
    'r' => "rectangle",
    's' => "square",
    'c' => "circle"
);

my @strings = qw(t r s c);

print "Input string : ";
chomp(my $string = <>);

die " Your input must be one of these strings : " , join ', ' , @strings unless $string ~~ @strings;
my $func = $switcher{$string};
my $area;

if($string ~~ @strings[0,1]) {
    print " Input n1 : ";
    chomp(my $n1 = <>);
    print " Input n2 : ";
    chomp(my $n2 = <>);
    $area  = &$func($n1,$n2);    
}elsif ($string ~~ @strings[2,3]) {
    print " Input n1 : ";
    chomp(my $n1 = <>);
    $area  = &$func($n1);  
}

print " Your $func area is $area \n" ;