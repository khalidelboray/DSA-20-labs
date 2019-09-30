sub triangle($a,$b) {
    return 0.5 * $a * $b;
}

sub rectangle($a,$b) {
    return $a * $b;
}

sub square($a) {
    return $a ** 2;
}

sub circle ($a) {
    return pi * ($a ** 2);
}
my $string = prompt("Inout string : ");
my $area = do given $string {
    when 't' {
        my $a = prompt("Input n1 : ");
        my $b = prompt("Input n2 : ");
        triangle($a,$b);
    }
    when 'r' {
        my $a = prompt("Input n1 : ");
        my $b = prompt("Input n2 : ");
        rectangle($a,$b);
    }
    when 's' {
        my $a = prompt("Input n1 : ");
        square($a);
    }
    when 'c' {
        my $a = prompt("Input n1 : ");
        circle($a);
    }
    default {
        note "Input valid string ";
        exit(1);
    }

}
put "Your area = $area ";