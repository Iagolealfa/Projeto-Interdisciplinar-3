# Colunas relevantes em cada tabela

### US Census Demographic Data
CensusTract: Census tract ID 
State: State, DC, or Puerto Rico 
County: County or county equivalent 
TotalPop: Total population 
Men: Number of men 
Women: Number of women 
Hispanic: percent of population that is Hispanic/Latino 
White: percent of population that is white 
Black: percent of population that is black 
Native: percent of population that is Native American or Native Alaskan 
Asian: percent of population that is Asian 
Pacific: percent of population that is Native Hawaiian or Pacific Islander Citizen: Number of citizens 
Income: Median household income 
IncomeErr: Median household income error 
IncomePerCap: Income per capita 
IncomePerCapErr: Income per capita error 
Poverty: percent under poverty level 
ChildPoverty: percent of children under poverty level
Professional: percent employed in management, business, science, and arts Service: percent employed in service jobs 
Office: percent employed in sales and office jobs 
Construction: percent employed in natural resources, construction, and maintenance 
Production: percent employed in production, transportation, and material movement 
Drive: percent commuting alone in a car, van, or truck 
Carpool: percent carpooling in a car, van, or truck 
Transit: percent commuting on public transportation 
Walk: percent walking to work 
OtherTransp: percent commuting via other means 
WorkAtHome: percent working at home 
MeanCommute: Mean commute time (minutes) 
Employed: percent employed (16+) 
PrivateWork: percent employed in private industry 
PublicWork: percent employed in public jobs 
SelfEmployed: percent self-employed 
FamilyWork: percent in unpaid family work 
Unemployment: Unemployment rate (percent)


### Fatal Encounters
Unique.ID
* Subject.s.age: Numérica Discreta
* Subject.s.gender: Categórica Nominal
* Subject.s.race: Categórica Nominal
* Subject.s.race.with.imputations: Categórica Nominal
Imputation.probability: Numéricas Discreta
URL.of.image.of.deceased
Date.of.injury.resulting.in.death..month.day.year.: Numéricas Discreta
Location.of.injury..address.
* Location.of.death..city.: Categórica Nominal
* Location.of.death..state.: Categórica Nominal
Location.of.death..zip.code.: Numéricas Discreta
Location.of.death..county.: Categórica Nominal
Full.Address: Categórica Nominal
? Latitude: Numéricas Discreta
? Longitude: Numéricas Discreta
Agency.responsible.for.death: Categórica Nominal
* Cause.of.death: Categórica Nominal
A.brief.description.of.the.circumstances.surrounding.the.death
* Dispositions.Exclusions.INTERNAL.USE..NOT.FOR.ANALYSIS: Categórica Nominal
* Intentional.Use.of.Force..Developing.: Categórica Nominal
* Symptoms.of.mental.illness..INTERNAL.USE..NOT.FOR.ANALYSIS: Categórica Nominal

* = coluna será usada no cluster
? = pode ser utilizada no cluster
# = feito


### Police Killings
Official.disposition.of.death..justified.or.other.
Criminal.Charges.
Unarmed.Did.Not.Have.an.Actual.Weapon
Alleged.Weapon..Source..WaPo.and.Review.of.Cases.Not.Included.in.WaPo.Database.
Alleged.Threat.Level..Source..WaPo.
Fleeing..Source..WaPo.
Body.Camera..Source..WaPo.
Off.Duty.Killing.
MPV.ID
Fatal.Encounters.ID