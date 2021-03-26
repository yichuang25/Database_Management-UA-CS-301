select essn, lname, pno 
from employee, works_on
where ssn = essn and Sex='M';

select essn, lname, pno
from(select * from employee where sex='M'), works_on
where ssn = essn;

select essn, lname, pno
from (select essn, lname, pno, sex from employee join works_on on ssn = essn)
where sex='M';



select fname, lname, dname, salary
from employee, department
where dno = dnumber
order by dno, salary desc;

--p35
select count(*)
from dependent
group by essn;

--p30
select dname, avg(salary)
from employee, department
where dno=dnumber
group by dname;

select dname, (select avg(salary) from employee where dno = dnumber) as AVERAGE_SALARY
from department;

--p31
select dname, avg(salary)
from department, employee
where dno = dnumber
group by dname
having avg(salary) > 32000;


select dname, avg(salary)
from department, employee
where dno = dnumber and (select avg(salary) from employee where dno=dnumber) > 32000
group by dname;

select dname, (select avg(salary) from employee where dno = dnumber group by dname having avg(salary) > 32000)
from department;



