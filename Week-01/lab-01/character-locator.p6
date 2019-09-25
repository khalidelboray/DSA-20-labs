
my $string = prompt("Input string : ");
my $chr = prompt("Input chr to look for : ");

# bla
say "Found $chr at indexes " ~ $string.indices($chr).join( ', ' );

sub locate_chr($string,$chr) {
    my @indexes;
    for ( 0 .. $string.chars - 1) -> $i {
        if $string.comb[$i] eq $chr {
            @indexes.push: $i;
        }
    }
    return @indexes;
}
say "Found $chr at indexes " ~ locate_chr($string,$chr).join( ', ' ) ~ " With loop ";