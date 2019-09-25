
my $num = prompt("Input start num : ");
my @list;
for ( 1 .. $num ) -> $i  {
    my @table;
    for (1 .. $i ) -> $k {
        @table.push: $i * $k;
    }
    @list.push: @table;
}
say @list;