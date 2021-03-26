--Natural join
select dname, dlocation
from department natural join dept_locations;

-- average salary and max salary
select avg(salary), max(salary)
from employee;

--name of employee salary grater than average
select lname, salary
from employee
where salary > (select avg(salary) from employee);

--name of employee salary grater than department average
select lname, salary
from employee e
where salary > (select avg(salary) from employee where dno = e.dno );

--each department name and average salary
select dname, avg(salary)
from employee, department
where dno = dnumber
group by dname;
--other way
select distinct dname, (select avg(salary) from employee where dno = e.dno) as dept_sal
from employee e, department
where dno = dnumber;
--third way
select dname, avg(salary)
from employee, department
where dno = dnumber
group by dname;


select dname, dno, avg(salary)
from employee, department
where dno = dnumber
group by dname, dno;


select dname, dno, avg(salary), count(*)
from employee, department
where dno = dnumber
group by dname, dno;

--average salary > 32000
select dname, avg(salary)
from employee, department
where dno = dnumber
group by dname
having avg(salary) > 32000;

select dname, avg(salary)
from employee, department
where dno = dnumber
group by dname
having avg(salary) > (select avg(salary) from employee);

--Case statement
