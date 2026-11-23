"""Task 5: semantic attachments and compositional beta-reduction examples."""
def semantic_attachments():
    return {'S -> NP VP':'VP(NP)','NP -> Name':'entity(name)','NP -> Det N':'lambda P: exists x (N(x) and P(x))','VP -> V NP':'V(object)','VP -> V':'lambda x: V(x)','PP -> P NP':'relation(P,NP)','VP -> VP PP':'attach_modifier(VP,PP)','NP -> NP and NP':'intersection(NP1,NP2)','S -> S and S':'and(S1,S2)','NP -> every N':'lambda P: forall x (N(x) -> P(x))','NP -> some N':'lambda P: exists x (N(x) and P(x))'}
def demo_derivations():
    return [
      {'sentence':'Ravi borrowed Atlas','steps':['lambda y. lambda x. Borrowed(x,y)','(lambda y. lambda x. Borrowed(x,y))(atlas)','lambda x. Borrowed(x,atlas)','(lambda x. Borrowed(x,atlas))(ravi)','Borrowed(ravi,atlas)'],'logical_form':'Borrowed(ravi,atlas)'},
      {'sentence':'Every employee receives some benefit','steps':['Compose subject NP and VP'],'logical_form':'forall x (Employee(x) -> exists y (Benefit(y) and Receives(x,y)))','alternate_scope':'exists y (Benefit(y) and forall x (Employee(x) -> Receives(x,y)))'},
      {'sentence':'Ravi is eligible for pension','steps':['Entity= ravi','Predicate= EligibleForPension'],'logical_form':'EligibleForPension(ravi)'},
      {'sentence':'Priya is a dependent of Ravi','steps':['Predicate= Dependent','Relation= RelatedTo'],'logical_form':'Dependent(priya) and RelatedTo(priya,ravi)'}]

if __name__ == "__main__":
    print("TASK 5 - SYNTAX-DRIVEN SEMANTIC ANALYSIS")
    print("\nSemantic attachment rules:")
    for rule, meaning in semantic_attachments().items():
        print(f"{rule} : {meaning}")
    print("\nSemantic derivations:")
    for item in demo_derivations():
        print("\nSentence:", item["sentence"])
        for i, step in enumerate(item["steps"], 1):
            print(f"  Step {i}: {step}")
        print("  Final logical form:", item["logical_form"])
        if "alternate_scope" in item:
            print("  Alternate scope:", item["alternate_scope"])
    print("\nTask 5 demo completed.")
