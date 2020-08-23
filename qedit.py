'''
open QU,'+<','quiz.txt' or die $!;
open AN,'+<','ans.txt' or die $!;
my @questions;
while (<QU>)
{
chomp;
my @temp = split ':';
push @questions,\@temp;
}

my @modque;
foreach my $temp1 (@questions)
{
	print 'Enter your question :';
	 $modque[0] = <STDIN>;
	 chomp($modque[0]);
	print 'Enter first choice :';
	 $modque[1] = <STDIN>;
	 chomp($modque[1]);
	print 'Enter Second choice :';
	 $modque[2] = <STDIN>;
	 chomp($modque[2]);
	print 'Enter Third choice :';
	 $modque[3] = <STDIN>;
	 chomp($modque[3]);
	print 'Enter Fourth choice :';
	 $modque[4] = <STDIN>;
	 chomp($modque[4]);
    @$temp1=@modque;
}
seek QU,0,0;
foreach (@questions){
	print QU join (":",@$_);
	print QU "\n";
}

my @answers;
while (<AN>)
{
chomp;
@answers = split ':';
}
my $tempans=0;
foreach (@answers){
	print"Enter the answer for respective question:";
	$answers[$tempans] = <STDIN>;
	chomp($answers[$tempans]);	
	$tempans++;
}

seek AN,0,0;
print AN join(":",@answers);
'''
qwrite=open("quiz.txt","w")
count =0;
temp=[];
while count < 5:
    tempque=input("Enter the question :")
    choise1=input("Enter the first choise :")
    choise2=input("Enter the second choise :")
    choise3=input("Enter the third choise :")
    choise4=input("Enter the fourth choise :")
    temp=[tempque,choise1,choise2,choise3,choise4]
    delim=":";
    qwrite.write(delim.join(temp))
    qwrite.write("\n")
    count=count + 1;
awrite=open("ans.txt","w")
ans1=input("Answer for first question :")
ans2=input("Answer for second question :")
ans3=input("Answer for third question :")
ans4=input("Answer for fouth question :")
ans5=input("Answer for fifth question :")

temp=[ans1,ans2,ans3,ans4,ans5]
awrite.write(delim.join(temp))



