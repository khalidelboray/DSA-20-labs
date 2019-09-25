use strict;
use warnings;

sub locate_chr {
    my ($string , $chr) = @_;
    my @chrs = split('',$string);
    my @indexs = ();
    for my $i (0.. length($string) - 1) {
        if($chrs[$i] eq $chr) {
            push @indexs , $i;
        }
    }
    @indexs;
}
print " Input String : ";
chomp(my $str = <>);
print " Input Char to look for : ";
chomp(my $chr = <>);

my @pos = locate_chr($str,$chr);

print "Found ". scalar @pos . " at indexes " , join ', ' , @pos;