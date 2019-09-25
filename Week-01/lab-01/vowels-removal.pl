use strict;
use warnings;
use experimental 'smartmatch';
my @vowels = qw(a e i o u);


# loop over all the string chars and check if it's a vowel
# if so , we replace it with an empty string

sub vowels_loop {
    my $string = shift;
    my @string_chars = split('',$string);
    for my $chr (@string_chars) {
        # lc($chr) string my have Upper Case chars 
        if (lc($chr) ~~ @vowels) {
            $string =~ s/$chr//;
        }
    }
    return $string;
}

# Search and replace using s/regex/replacement/modifiers
# see https://perldoc.perl.org/perlrequick.html
# 

sub vowels_regex {
    my $string = shift;
    # g modifier will search and replace all occurrences of the regex in the string
    # i modifier used to search in a case-insensitive way
    $string =~ s/[aeiou]//gi;
    return $string;
}

print " Input your string : ";
chomp(my $string = <>);

print "Using loop over string chars.\n";
my $s = vowels_loop($string);
print "\tString was '$string' and Became '$s' \n";

print "Using search and replace with regex.\n";
$s = vowels_regex($string);
print "\tString was '$string' and Became '$s' \n";