"""Task 11: transparent design comparison template based on observed demo capabilities."""
OPTIONS={
 "reference_resolution":[("Hobbs-style syntax search","uses parse structure","parser-dependent"),
                         ("Centering Theory","models discourse salience","needs discourse state")],
 "dialogue":[("finite-state","predictable and easy to test","rigid paths"),
             ("frame-based","handles slot filling and corrections","requires slot schema")],
 "generation":[("template","high control","limited variety"),
               ("planning + realisation","content order is explicit","more components to maintain")],
 "translation":[("transfer","domain rules can preserve key terms","language-pair rules scale"),
                ("interlingua","shared semantic representation","building interlingua is costly"),
                ("statistical","learns lexical correspondences","needs large parallel corpus")]
}
def main():
    print("TASK 11 - DESIGN COMPARISON")
    for layer,rows in OPTIONS.items():
        print("\n",layer.upper())
        for name,benefit,risk in rows: print(f"{name}: advantage={benefit}; limitation={risk}")
    print("\nRecommendation: hybrid, confidence-aware system; retain human approval for life-safety alerts, evacuation orders, shelter availability and translated emergency instructions.")
    print("No numerical winner is claimed because a comparable held-out evaluation has not yet been run.")
if __name__=="__main__": main()
