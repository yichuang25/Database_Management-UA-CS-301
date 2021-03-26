select * 
from department natural join dept_locations; 

select * 
from department join dept_locations on department.dnumber = dept_locations.dnumber;


--p39
select * from employee where dno<>4;

select dno 
from employee 
where dno not in (select dno from employee where sex = 'F');

describe employee;

