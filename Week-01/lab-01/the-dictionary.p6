my @names = <ali ahmed ibrahim islam fatma fahim fadi>;
my %dic;
for @names -> $name {
    my $let = $name.comb[0];
    %dic{$let}.push: $name;
}
say %dic