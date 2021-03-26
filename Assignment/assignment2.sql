select *
from works_on
where hours > 25;

select essn, pno, pname
from works_on
join project
on pnumber = pno
where hours>25