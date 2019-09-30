my $num = prompt("Input number : ");
for (0..$num) -> $i {
    print ' ' x ($num - $i);
    put '*' x $i;
}