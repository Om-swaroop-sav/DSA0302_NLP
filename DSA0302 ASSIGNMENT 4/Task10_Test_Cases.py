from Task03_FOPC_Knowledge_Base import demo
from Task05_Syntax_Driven_Semantic_Analysis import demo_derivations
from Task07_Word_Sense_Disambiguation import lesk
from Task12_Temporal_Pension_Rules import scheme_on
from datetime import date
def run():
 _,c=demo(); assert c['Ravi qualifies (12 years)'] and c['Priya qualifies as family pensioner'] and not c['Kumar qualifies']
 assert demo_derivations()[0]['logical_form']=='Borrowed(ravi,atlas)'
 assert lesk('dependent','A dependent child may receive family pension.')[0]=='family_member'
 assert scheme_on(date(2019,6,1))['name']=='old' and scheme_on(date(2022,6,1))['name']=='revised'
 print('All demo tests passed.')
if __name__=='__main__':run()
