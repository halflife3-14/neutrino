'''
open FH,'<','Database.txt' or die $!;
my %users;
while (<FH>)
{
chomp;
my ($username, @datas) = split ':';
$users{$username} = \@datas;
}

print "Enter your username :";
my $loginuser =<STDIN>;
chomp ($loginuser);
# $\ ="\n";	
if (exists $users{$loginuser})
	{
foreach ( sort keys %users)
{
	my $local = $loginuser eq $_;
	# print $local;
    if ($local == 1)
	{
	print "Password :";
	my $loginpass = <STDIN>;
	chomp($loginpass);
	if ($loginpass eq ${$users{$_}}[0])
		{
         print "Successfully logged in\n";
		 print "Your test score : ${$users{$_}}[1]\n";
		}
	else
	{
		print 'Login Error';
		exit;
	}
    }
}
	}
else {
	print 'Username error';
}
close FH;
print 'Do you want to edit the Questions(y/n):';
my $qeditans =<STDIN>;
chomp($qeditans);
if ($qeditans eq 'y'){
	questionedit();
	print"Thank you\n";
	exit;
}
else{
	print"Terminating the program.See you later\n";
	exit;
}
close QU;
'''
register={};
with open ("Database.txt","r") as database:
       users=database.readlines()
       for members in users:
        temp=members.split(":")
        temp2=[temp[1],temp[2]]
        register[temp[0]]=temp2  
        
username=input("Enter your username :")
password=input("Enter your password :")
for keys1 in register.keys():
    if username == keys1:
       if password == register[keys1][0]:
        print("logged in")
        print("Your score is",register[keys1][1])
        exit()
        

print("Username or Password error")