class ADA:
    def __init__(self,fee):
        self.fee = fee 
        
class CN:
    def __init__(self,students):
        self.students = students
class OS:
    def __init__(self,batches):
        self.batches = batches 
class Assignments:
    def __init__(self):
        self.ada = None 
        self.cn = None 
        self.os = None 
    def specifications(self):
        return f"ada :{self.ada.fee} \n cn :{self.cn.students}\n os :{self.os.batches}"
subject =Assignments ()
subject.ada = ADA(10000)
subject.cn = CN(2311133)
subject.os = OS(3)
print(subject.specifications()) 


class Subjects:
    def add_subjects(self):
        pass  
    def add_ada(self):
        pass 
    def add_os(self):
        pass 
    def add_cn(self):
        pass 

class subjectsBuild(Subjects):
    def __init__(self):
        self.Assignments = Assignments()
    def add_ada(self):
        ada = ADA("chapter 1")
        self.Assignments.ada = ada  
        return self 
    def add_cn(self):
        ada = CN("chapter 2")
        self.Assignments.cn = CN 
        return self 
    def add_os(self):
        ada = OS("chapter 3")
        self.Assignments.os = OS
        return self 
    def build(self):
        return self.Assignments 
class Final:
    def __init__(self,subjects_builder):
        self.subjects_builder = subjects_builder 
    def get_subjects(self):
        return self.subjects_builder.add_ada().add_cn().add_os()

            
    
        