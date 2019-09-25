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

my @pos = locate_chr("Hey There",'e');

print "Found ". scalar @pos . " at indexes " , join ', ' , @pos;