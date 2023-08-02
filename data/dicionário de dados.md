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
Subject.s.age *#
Subject.s.gender *#
Subject.s.race *
Subject.s.race.with.imputations *
Imputation.probability
URL.of.image.of.deceased
Date.of.injury.resulting.in.death..month.day.year.
Location.of.injury..address.
Location.of.death..city. *
Location.of.death..state. *
Location.of.death..zip.code.
Location.of.death..county.
Full.Address
Latitude ?
Longitude ?
Agency.responsible.for.death
Cause.of.death *#
A.brief.description.of.the.circumstances.surrounding.the.death
Dispositions.Exclusions.INTERNAL.USE..NOT.FOR.ANALYSIS *
Intentional.Use.of.Force..Developing. *#
Symptoms.of.mental.illness..INTERNAL.USE..NOT.FOR.ANALYSIS *

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