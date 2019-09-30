my @sites = ( 'https://google.com', 'https://github.com', 'https://gitlab.com');
my $cho = @sites.pick;
put "Opening $cho in chrome ";
shell "start chrome $cho"