--1.a
select distinct ssn, salary
from employee, department
where salary < 30000 or dno = dnumber and dname = 'Administration';

--1.b
select ssn, salary
from employee join department on dname = 'Administration'
where salary < 30000 or dno = dnumber;

--1.c
select distinct ssn, salary
from employee, department
where salary < 30000 or dno in (select dnumber from department where dname = 'Administration');

--1.d
select ssn, salary
from employee
where salary < 30000 or dno = any (select dnumber from department where dname = 'Administration');

--1.e
select ssn, salary
from employee
where salary < 30000 or exists (select dnumber from department where dname = 'Administration' and dno = dnumber);

--1.f
select ssn, salary
from (  select ssn, salary
        from employee join department on dname = 'Administration'
        where salary < 30000 or dno = dnumber);
    
--2.
select distinct pnumber  as project_number, dnum as Controlling_department_number, lname as Last_name, address, bdate as Birth_Date
from employee, project, department
where plocation = 'Stafford' and dnumber = dnum and MGRSSN = SSN;

--3.a   
select dname, dlocation, plocation, pnumber
from project, dept_locations, department
where dnum = dept_locations.dnumber and dnum = department.dnumber and plocation = dlocation;

--3.b
select dname, dlocation, plocation, pnumber
from department natural join dept_locations l, project
where dlocation = plocation and dnumber = dnum;

--4.a
select essn
from works_on
where hours > 30
intersect
select essn 
from works_on
where hours < 10 and essn in (select essn from works_on where hours > 30);

--4.b
select essn
from works_on less
where less.hours > 30 and less.essn in(select essn from works_on more where more.hours < 10 and less.pno <> more.pno);

--4.c
select essn
from works_on
where hours < 10
union
select essn
from works_on
where hours > 30;

--4.d
select distinct essn
from works_on
where hours < 10 or hours > 30;

--5.a
select ssn, fname, lname
from employee
where ssn IN (
select ssn
from employee
minus
select distinct essn from dependent where relationship = 'Spouse');

--5.b

select ssn, fname, lname
from employee
where ssn not in (select essn from dependent where relationship = 'Spouse');

--6.
select fname, lname, floor(((sysdate - TO_DATE(bdate,'yyyy-mm-dd'))/365)) as age
from employee
ORDER by age DESC;

--7.
select round(AVG(((sysdate - TO_DATE(bdate,'yyyy-mm-dd'))/365))) as Average_Age
from employee;

--8.a
SELECT Lname, Fname, count(*) Number_Of_Projects
FROM EMPLOYEE, works_on
WHERE essn = ssn
group by lname, fname;

--8.b
SELECT Lname, Fname, count(*) Number_Of_Projects_More_Than_2
FROM EMPLOYEE, works_on
WHERE essn = ssn
group by lname, fname
having count(*) >= 2;

--8.c
--insert into employee values ('Tom', 'C' ,'Doe', 555554444, '1999-03-06', '1891 Water,Tuscaloosa,AL','M',50000,333445555,4);

--delete from employee
--where Fname = 'Tom';

--select *
--from employee;

SELECT Lname, Fname, count(essn) Number_Of_Projects
FROM EMPLOYEE left join works_on on ssn =essn
group by lname, fname;

--9.a
select essn, pname, hours
from works_on, project
where pno = pnumber and hours > (select avg(hours) from works_on);

--9.b
select pname, avg(hours)
from works_on, project
where pno = pnumber
group by pname;

--9.c
select pname, avg(hours)
from works_on, project
where pno = pnumber
group by pname
having avg(hours) < (select avg(hours) from works_on);


--10.
select lname, fname, (select count(*) from works_on where e.ssn = essn) as Number_of_project
from employee e;
