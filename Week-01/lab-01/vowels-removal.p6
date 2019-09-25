
#| get non vowels using .comb and regex 
sub vowels_non ($string is copy) {
    $string = $string.comb(/<-[a e i o u]>+/).join;
    $string;
}

#| replace all vowels with an empty string
sub vowels_replace ($string is copy) {
    $string .= subst(/<[aeiou]>/,'',:g);
    $string;
}

my $string = prompt("Input your string : ");

put vowels_non($string);
put vowels_replace($string);