my @sites = ('https://google.com','https://github.com','https://gitlab.com');
my $cho = $sites[rand @sites];
print "Opening $cho in chrome \n";
system("start chrome $cho")