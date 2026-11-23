"""Task 3: small FOPC-style fact base, model checks and forward inference."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Fact:
    predicate:str
    args:tuple
class KnowledgeBase:
    def __init__(self): self.facts=set()
    def add(self,p,*a): self.facts.add(Fact(p,tuple(a)))
    def has(self,p,*a): return Fact(p,tuple(a)) in self.facts
    def infer(self):
        changed=True
        while changed:
            changed=False
            for f in list(self.facts):
                new=[]
                if f.predicate=='completed_years' and f.args[1]>=10: new=[Fact('eligible_retirement_pension',(f.args[0],))]
                if f.predicate=='spouse_of' and Fact('deceased',(f.args[1],)) in self.facts: new=[Fact('eligible_family_pension',f.args)]
                for x in new:
                    if x not in self.facts: self.facts.add(x); changed=True
        return self.facts
def demo():
    k=KnowledgeBase(); k.add('employee','ravi'); k.add('completed_years','ravi',12); k.add('spouse_of','priya','ravi'); k.add('deceased','ravi'); k.infer()
    return k,{'Ravi qualifies (12 years)':k.has('eligible_retirement_pension','ravi'),'Priya qualifies as family pensioner':k.has('eligible_family_pension','priya','ravi'),'Kumar qualifies':k.has('eligible_retirement_pension','kumar')}
if __name__=='__main__':
    _,r=demo(); [print(k,':',v) for k,v in r.items()]
