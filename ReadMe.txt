Problem states that given N female and N males, where each person has ranked all members of the opposite sex in order of preference, date the males and females together such that there are no two people of opposite sex who would both rather have each other than their current partners.
Let there be two male m1 and m2 and two female f1 and f2.
Let m1‘s list of preferences be {f1, f2}
Let m2‘s list of preferences be {f1, f2}
Let f1‘s list of preferences be {m1, m2}
Let f2‘s list of preferences be {m1, m2}

The matching { {m1, f2}, {f1, m2} } is not stable because m1 and f1 would prefer each other over their assigned partners. The matching {m1, f1} and {m2, f2} is stable because there are no two people of opposite sex that would prefer each other over their assigned partners.

The preferances are based on the compatiblity questions. We assigned first option of each compatibility question as 1 and second option as 0.
We calculate the sum for each male and female.
for female f1
if difference of sum of compatibility of m1 and f1 is less than difference of sum of compatibility of m2 and f1
then f1 first preference will be m1 then m2 
Same logic is applicable for every male and female