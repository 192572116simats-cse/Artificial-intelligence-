% Student-Teacher-Subject Database

student(101, 'Aishwarya').
student(102, 'Rahul').
student(103, 'Priya').

teacher('Dr_Kumar', 'CSA101').
teacher('Mrs_Priya', 'CSA102').
teacher('Mr_Arun', 'CSA103').

subject('CSA101', 'Artificial_Intelligence').
subject('CSA102', 'Python_Programming').
subject('CSA103', 'Database_Management').

details(Student, Teacher, Code, Subject) :-
    student(_, Student),
    teacher(Teacher, Code),
    subject(Code, Subject).
