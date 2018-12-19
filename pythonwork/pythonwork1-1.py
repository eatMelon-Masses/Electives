import random;
 
def has_duplicates(t):
    s = t[:]; #make a copy of original list
    s.sort();
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True;
    return False;
 
def genarate_birthdy(numbers):
    birthday_list = [];
    for i in range(numbers):
        birthday_list.append(random.randint(1,365));
    return birthday_list;
 
def count_matches(student,samples):
    count = 0;
    t= []
    for i in range(samples):
        t= genarate_birthdy(student);
        if has_duplicates(t):
            count+=1
 
    return count;
 
num_students = 23;
numb_simulations= 1000000;
 
count = count_matches(num_students,numb_simulations);
rate = float(count)/numb_simulations*100
 
print ('After %d simulations'%numb_simulations);
print ('with %d student'%num_students);
print ('there were %d simulations with at least one match' %count);
print ('rate is %f'%rate);